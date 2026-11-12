from pathlib import Path

ROOT = Path(__file__).parent
METADATA_DIR = ROOT / "data" / "raw" / "metadata"

CATEGORY = "quant-ph"
DATE_START = "201801010000"
DATE_END = "202512312359"

# One query per subtopic. These terms are a starting point, so tune them.
SUBTOPICS = {
    "foundations": ["foundations of quantum mechanics", "quantum foundations"],
    "measurement": ["measurement problem", "wave function collapse", "quantum measurement"],
    "interpretations": ["Copenhagen interpretation", "many-worlds", "Bohmian", "QBism",
                        "relational quantum mechanics", "interpretations of quantum mechanics"],
    "decoherence": ["decoherence", "quantum-to-classical transition", "einselection"],
    "bell_epr": ["Bell theorem", "EPR paradox", "Bell nonlocality"],
    "contextuality": ["contextuality", "Kochen-Specker"],
    "uncertainty": ["uncertainty relation", "uncertainty principle", "complementarity"],
}
PER_SUBTOPIC = 80

# Review/tutorial query: title terms AND a foundations term in the abstract
REVIEW_CATEGORIES = ["quant-ph", "physics.hist-ph", "physics.ed-ph"]
REVIEW_TITLE_TERMS = ["review", "tutorial", "lecture notes", "introduction to",
                      "pedagogical", "primer"]
REVIEW_TOPIC_TERMS = ["quantum foundations", "foundations of quantum", "interpretation",
                      "measurement problem", "decoherence", "Bell", "nonlocality",
                      "contextuality", "EPR", "uncertainty", "wave function"]
REVIEW_MAX = 150