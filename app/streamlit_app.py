import datetime
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from groq import APIConnectionError, RateLimitError

from src.generate import answer
from src.retrieve import _load

GITHUB_URL = "https://github.com/jatinxvats/schrodingers-librarian"
MAX_PER_SESSION = 10
MAX_PER_DAY = 300

st.set_page_config(page_title="Schrödinger's Librarian", page_icon="📚")

EXAMPLES = [
    ("Copenhagen vs many-worlds",
     "What is the fundamental difference between the Copenhagen and many-worlds interpretations?"),
    ("Is an observer needed?", "Is an observer required for the wave function to collapse?"),
    ("What is decoherence?", "What is decoherence?"),
]


@st.cache_resource
def warm_up():
    _load()  # load MiniLM and Chroma once per server process
    return True


@st.cache_resource
def daily_counter():
    return {"day": None, "n": 0, "lock": threading.Lock()}


def take_daily_slot() -> bool:
    c = daily_counter()
    today = datetime.date.today()
    with c["lock"]:
        if c["day"] != today:
            c["day"], c["n"] = today, 0
        if c["n"] >= MAX_PER_DAY:
            return False
        c["n"] += 1
        return True


def group_sources(sources: list[dict]) -> list[list[dict]]:
    """One group per paper, in order of first appearance."""
    papers: dict[str, list[dict]] = {}
    for s in sources:
        papers.setdefault(s["paper_id"], []).append(s)
    return list(papers.values())


warm_up()

for key, default in (("q", ""), ("auto_run", False), ("asked", 0)):
    st.session_state.setdefault(key, default)

# ---------- sidebar ----------
with st.sidebar:
    st.header("About")
    st.write(
        "Answers questions about the foundations of quantum mechanics from"
        "arXiv papers, with citations to the passages used."
    )
    st.subheader("How it works")
    st.markdown(
        "1. Your question is matched to passages in the papers.\n"
        "2. A language model answers using only those passages and cites them.\n"
        "3. If nothing relevant is found, it says so."
    )
    st.subheader("Limits")
    st.markdown(
        "- Sources are unreviewed preprints.\n"
        "- The answer is written by an AI and can misattribute a view or stretch a source.\n"
        "- Display equations were removed when the papers were processed.\n"
        "- Contested questions get several views with no verdict.\n"
        "- The corpus covers measurement, interpretations, Bell/EPR, decoherence, "
        "contextuality and uncertainty, and little else."
    )
    st.markdown(f"[Source code and evaluation]({GITHUB_URL})")
    counter_slot = st.empty()


def show_left():
    left = max(0, MAX_PER_SESSION - st.session_state.asked)
    counter_slot.caption(f"Questions left this session: {left}")


show_left()

# ---------- main ----------
st.title("📚 Schrödinger's Librarian")
st.caption("Ask about quantum foundations.")

st.write("Try an example:")
cols = st.columns(len(EXAMPLES))
for i, (label, ex) in enumerate(EXAMPLES):
    if cols[i].button(label, key=f"ex{i}", use_container_width=True):
        st.session_state.q = ex
        st.session_state.auto_run = True

question = st.text_input("Your question", key="q", max_chars=500)
asked = st.button("Ask", type="primary")
run = asked or st.session_state.auto_run
st.session_state.auto_run = False

if run and len(question.strip()) >= 3:
    if st.session_state.asked >= MAX_PER_SESSION:
        st.warning(
            f"You've used your {MAX_PER_SESSION} questions for this session. "
            "Come back later, or run it yourself from the GitHub repo."
        )
        st.stop()
    if not take_daily_slot():
        st.warning("The demo has reached its daily question limit. Please try again tomorrow.")
        st.stop()
    st.session_state.asked += 1
    show_left()

    with st.spinner("Searching papers..."):
        try:
            result = answer(question.strip())
        except RateLimitError:
            st.warning("The language model is rate-limited right now. Wait a minute and try again.")
            st.stop()
        except APIConnectionError:
            st.error("Couldn't reach the language model service. Please try again.")
            st.stop()
        except Exception as e:
            st.error(f"Something went wrong ({type(e).__name__}). Please try again.")
            st.stop()

    with st.container(border=True):
        st.markdown(result["answer"])

    if result["sources"]:
        cited = set(result["citations"]["cited"])
        st.subheader("Sources")
        st.caption("Open a passage to check the claim against the paper's own words.")
        for group in group_sources(result["sources"]):
            first = group[0]
            nums = ", ".join(f"[{s['n']}]" for s in group)
            flag = "✅ cited" if any(s["n"] in cited for s in group) else "retrieved, not cited"
            st.markdown(
                f"**{nums}** [{first['title']}]({first['pdf_url']}) — {first['authors']}, "
                f"{first['date']} · {flag}"
            )
            for s in group:
                mark = " ✅" if s["n"] in cited else ""
                with st.expander(f"Show retrieved text [{s['n']}]{mark}"):
                    st.text(s["text"])
        if result["citations"]["invalid"]:
            st.warning(
                "The answer cites a source number that doesn't exist: "
                f"{result['citations']['invalid']}"
            )