import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "questions_skeleton.json"

# (bucket, type, question)
QUESTIONS = [
    # definition (12)
    ("foundations", "definition", "What is a Hilbert space?"),
    ("bell_epr", "definition", "What does Bell's theorem rule out?"),
    ("contextuality", "definition", "What is the Kochen-Specker theorem?"),
    ("contextuality", "definition", "What does it mean for quantum mechanics to be contextual?"),
    ("decoherence", "definition", "What is decoherence?"),
    ("measurement", "definition", "What is the measurement problem in quantum mechanics?"),
    ("measurement", "definition", "What is the Born rule?"),
    ("uncertainty", "definition", "What does the Heisenberg uncertainty principle actually say?"),
    ("bell_epr", "definition", "What is the EPR paradox?"),
    ("foundations", "definition", "What is the Frauchiger-Renner paradox?"),
    ("interpretations", "definition", "What is Bohmian mechanics?"),
    ("decoherence", "definition", "What is quantum Darwinism?"),
    # comparison (10)
    ("interpretations", "comparison", "What is the fundamental difference between the Copenhagen interpretation and the many-worlds interpretation?"),
    ("interpretations", "comparison", "How does Bohmian mechanics differ from standard quantum mechanics in how it treats particles?"),
    ("contextuality", "comparison", "How is quantum contextuality different from Bell nonlocality?"),
    ("uncertainty", "comparison", "Is the uncertainty principle the same thing as the observer effect?"),
    ("decoherence", "comparison", "How does decoherence differ from wave function collapse?"),
    ("interpretations", "comparison", "How do objective collapse theories differ from the many-worlds interpretation?"),
    ("interpretations", "comparison", "How does QBism differ from the Copenhagen interpretation?"),
    ("bell_epr", "comparison", "What is the difference between entanglement and Bell nonlocality?"),
    ("contextuality", "comparison", "How do local hidden variable models differ from noncontextual hidden variable models?"),
    ("uncertainty", "comparison", "How do Heisenberg's and Robertson's uncertainty relations differ?"),
    # contested (10)
    ("measurement", "contested", "Is an observer required for the wave function to collapse?"),
    ("measurement", "contested", "Does collapse really take place, and how could it be scientifically verified?"),
    ("foundations", "contested", "Does the wave function describe physical reality or only our knowledge?"),
    ("bell_epr", "contested", "Is quantum mechanics a complete description of reality?"),
    ("bell_epr", "contested", "Does Bell's theorem prove that nature is nonlocal?"),
    ("decoherence", "contested", "Does decoherence solve the measurement problem?"),
    ("measurement", "contested", "Can the Born rule be derived, or is it a postulate?"),
    ("interpretations", "contested", "How can probabilities make sense in the many-worlds interpretation?"),
    ("uncertainty", "contested", "Is the uncertainty principle caused by measurement disturbance, or is it intrinsic to quantum systems?"),
    ("decoherence", "contested", "Is there a boundary between the quantum and classical worlds?"),
    # multi-topic (6)
    ("multi", "multi", "How do decoherence and many-worlds together explain why we see definite outcomes?"),
    ("multi", "multi", "How are contextuality, the Kochen-Specker theorem and Bell nonlocality related?"),
    ("multi", "multi", "Which experiments have tested whether quantum mechanics is nonlocal, and what do they conclude?"),
    ("multi", "multi", "How are uncertainty relations related to complementarity and measurement disturbance?"),
    ("multi", "multi", "What does the Frauchiger-Renner paradox imply for interpretations of quantum mechanics?"),
    ("multi", "multi", "How does Bohmian mechanics deal with both measurement and nonlocality?"),
    # unanswerable, out of domain (6)
    ("none", "unanswerable", "How does a nuclear reactor work?"),
    ("none", "unanswerable", "What is the current price of Bitcoin?"),
    ("none", "unanswerable", "What is the boiling point of liquid nitrogen?"),
    ("none", "unanswerable", "How do vaccines train the immune system?"),
    ("none", "unanswerable", "What causes the aurora borealis?"),
    ("none", "unanswerable", "Who discovered penicillin?"),
    # unanswerable, near domain (6): VERIFY the corpus really lacks each fact
    ("decoherence", "unanswerable", "What is the numerical value of the CSL collapse rate parameter?"),
    ("decoherence", "unanswerable", "How long does a dust grain stay coherent at room temperature?"),
    ("bell_epr", "unanswerable", "What detection efficiency did the 2015 loophole-free Bell tests achieve?"),
    ("decoherence", "unanswerable", "What is the largest object that has been put in a quantum superposition experimentally?"),
    ("measurement", "unanswerable", "To what precision has the Born rule been verified experimentally?"),
    ("bell_epr", "unanswerable", "What error rate do current quantum computers achieve when preparing Bell states?"),
]

entries = [
    {
        "id": i,
        "bucket": b,
        "type": t,
        "question": q,
        "answerable": t != "unanswerable",
        "relevant_papers": [],
        "must_include": "",
        "notes": "",
    }
    for i, (b, t, q) in enumerate(QUESTIONS, 1)
]
assert len(entries) == 50
OUT.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"wrote {len(entries)} questions to {OUT}")