import json
from pathlib import Path
from typing import Dict, Any

PATTERNS_FILE = Path(__file__).resolve().parent.parent / "data" / "patterns.json"


def load_patterns() -> list[dict]:
    if not PATTERNS_FILE.exists():
        raise FileNotFoundError(f"patterns.json not found at {PATTERNS_FILE}")

    with open(PATTERNS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_pattern_details(pattern_name: str) -> Dict[str, Any]:
    patterns = load_patterns()

    for pattern in patterns:
        if pattern["name"] == pattern_name:
            return pattern

    raise ValueError(f"No pattern found for '{pattern_name}'")