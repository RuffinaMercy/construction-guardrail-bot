CONSTRUCTION_KEYWORDS = {
    "construction", "building", "house", "home", "structure", "project", "site",

    "cement", "concrete", "sand", "aggregate", "steel", "brick", "blocks",
    "tiles", "marble", "granite", "wood", "glass", "paint",

    "foundation", "footing", "column", "beam", "slab", "roof", "wall",
    "floor", "ceiling", "plaster", "reinforcement", "rcc",

    "design", "plan", "layout", "elevation", "drawing", "load",
    "strength", "durability", "stability",

    "cost", "budget", "estimate", "price", "expense", "rate",
    "quotation", "bill", "contract",

    "excavation", "curing", "mixing", "casting", "formwork",
    "shuttering", "compaction",

    "soil", "clay", "sand soil", "black cotton soil",
    "raft", "pile", "isolated", "combined",

    "crack", "leak", "seepage", "damp", "failure",
    "settlement", "corrosion",

    "safety", "helmet", "scaffold", "hazard", "risk", "protection",

    "plumbing", "electrical", "wiring", "drainage", "pipeline",

    "contractor", "labour", "equipment", "machine", "tools"
}


def is_valid_query(query: str, domain_check=False) -> bool:
    if not query or len(query.strip()) < 3:
        return False

    if domain_check:
        words = set(query.split())
        match_count = len(words.intersection(CONSTRUCTION_KEYWORDS))

        # smarter filtering
        if match_count == 0:
            return False

        return True

    return True