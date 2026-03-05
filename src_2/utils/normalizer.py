import re

def normalize_query(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)

    replacements = {
        # General
        "bldg": "building",
        "proj": "project",
        "const": "construction",

        # Materials
        "conc": "concrete",
        "cementing": "cement",
        "agg": "aggregate",
        "rebars": "steel reinforcement",
        "rcc": "reinforced concrete",

        # Structural Elements
        "col": "column",
        "beam col": "beam column",
        "fdn": "foundation",
        "footing": "foundation",

        # Units
        "sqft": "square feet",
        "sq ft": "square feet",
        "sqm": "square meter",
        "sq m": "square meter",

        # Cost
        "est": "estimate",
        "approx": "approximate",
        "amt": "amount",

        # Issues
        "crk": "crack",
        "leakage": "leak",
        "dampness": "damp",

        # Utilities
        "elec": "electrical",
        "plumb": "plumbing",

        # Informal
        "u": "you",
        "pls": "please",
    }

    # Word-based replacement (prevents "col" → "color" bug)
    for k, v in replacements.items():
        text = re.sub(rf"\b{k}\b", v, text)

    # Remove special characters
    text = re.sub(r"[^a-z0-9\s]", "", text)

    return text