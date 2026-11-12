import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from groq import APIConnectionError, RateLimitError

from src.generate import answer
from src.retrieve import _load

st.set_page_config(page_title="Schrödinger's Librarian", page_icon="📚")

EXAMPLES = [
    "What is the fundamental difference between the Copenhagen and many-worlds interpretations?",
    "Is an observer required for the wave function to collapse?",
    "Does collapse really take place, and how could it be verified?",
]


@st.cache_resource
def warm_up():
    _load()  # load MiniLM and Chroma once per server process
    return True


def group_sources(sources: list[dict]) -> list[list[dict]]:
    """One group per paper, in order of first appearance."""
    papers: dict[str, list[dict]] = {}
    for s in sources:
        papers.setdefault(s["paper_id"], []).append(s)
    return list(papers.values())


warm_up()

st.title("Schrödinger's Librarian")
st.caption(
    "Questions about the foundations of quantum mechanics, answered from about 110 "
    "arXiv papers, with citations."
)
st.info(
    "Sources are unreviewed arXiv preprints, and the answer is written by an AI model. "
    "It can misattribute views or overstate what a paper says. Check the retrieved "
    "text under each source before relying on a claim."
)

if "q" not in st.session_state:
    st.session_state.q = ""
if "auto_run" not in st.session_state:
    st.session_state.auto_run = False

st.write("Try an example:")
for i, ex in enumerate(EXAMPLES):
    if st.button(ex, key=f"ex{i}", use_container_width=True):
        st.session_state.q = ex
        st.session_state.auto_run = True

question = st.text_input("Your question", key="q", max_chars=500)
asked = st.button("Ask", type="primary")
run = asked or st.session_state.auto_run
st.session_state.auto_run = False

if run and len(question.strip()) >= 3:
    with st.spinner("Searching papers..."):
        try:
            result = answer(question.strip())
        except RateLimitError:
            st.warning("The language model is rate-limited right now. Wait a minute and try again.")
            st.stop()
        except APIConnectionError:
            st.error("Couldn't reach the language model service. Check your connection and try again.")
            st.stop()
        except Exception as e:
            st.error(f"Something went wrong ({type(e).__name__}). Please try again.")
            st.stop()

    st.markdown(result["answer"])

    if result["sources"]:
        cited = set(result["citations"]["cited"])
        st.subheader("Sources")
        for group in group_sources(result["sources"]):
            first = group[0]
            nums = ", ".join(f"[{s['n']}]" for s in group)
            flag = "✅ cited" if any(s["n"] in cited for s in group) else "retrieved, not cited"
            st.markdown(
                f"**{nums}** [{first['title']}]({first['pdf_url']}) — {first['authors']}, "
                f"{first['date']} · best distance {min(s['distance'] for s in group)} · {flag}"
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