'''
    given a input problem description/statement along with optional testcases/egamples and problem constrainsts
    use them to classify the given problem as one of the predefined patterns
'''

import json
from typing import List, Optional
from app.utils.json_utils import parse_json_response
from anthropic import Anthropic

from app.config import (
    ANTHROPIC_API_KEY,
    CLAUDE_MODEL,
    MAX_CLASSIFIER_TOKENS,
    CLASSIFIER_TEMPERATURE,
)


ALLOWED_PATTERNS: List[str] = [
    "arrays",
    "strings",
    "hash_map",
    "two_pointers",
    "sliding_window",
    "binary_search",
    "stack",
    "queue",
    "linked_list",
    "tree",
    "graph",
    "heap_priority_queue",
    "backtracking",
    "greedy",
    "dynamic_programming",
    "recursion",
    "matrix",
    "bit_manipulation",
]

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def _format_optional_section(title: str, content: Optional[str]) -> str:
    if not content or not content.strip():
        return f"{title}: Not provided"
    return f"{title}:\n{content.strip()}"


def _build_classifier_prompt(
    problem_statement: str,
    examples: Optional[str] = None,
    constraints: Optional[str] = None,
) -> str:
    allowed_patterns_str = ", ".join(ALLOWED_PATTERNS)

    return f"""
You are an expert algorithm problem classifier.

Your task is to classify the given coding problem into exactly one predefined problem-solving pattern.

Allowed patterns:
{allowed_patterns_str}

Rules:
- Choose exactly one pattern from the allowed patterns list.
- Use the problem statement primarily.
- Use examples and constraints as supporting information if provided.
- Prefer the dominant solving pattern.
- If multiple patterns seem possible, choose the one most likely to produce the standard interview solution.
- Return valid JSON only.
- Do not include markdown or extra explanation outside JSON.

Return format:
{{
  "pattern": "one_of_the_allowed_patterns",
  "confidence": 0.0,
  "reason": "short reason for why this pattern fits"
}}

Confidence must be a float between 0.0 and 1.0.

Problem Statement:
{problem_statement.strip()}

{_format_optional_section("Examples / Test Cases", examples)}

{_format_optional_section("Constraints", constraints)}
""".strip()




def _safe_parse_classifier_output(raw_text: str) -> dict:
    parsed = parse_json_response(raw_text)

    if not isinstance(parsed, dict):
        raise ValueError("Classifier output must be a JSON object.")

    pattern = parsed.get("pattern")
    confidence = parsed.get("confidence")
    reason = parsed.get("reason")

    if pattern not in ALLOWED_PATTERNS:
        raise ValueError(
            f"Invalid pattern '{pattern}'. Allowed patterns: {ALLOWED_PATTERNS}"
        )

    if not isinstance(confidence, (int, float)) or not (0.0 <= float(confidence) <= 1.0):
        raise ValueError("Confidence must be a float between 0.0 and 1.0.")

    if not isinstance(reason, str) or not reason.strip():
        raise ValueError("Reason must be a non-empty string.")

    return {
        "pattern": pattern,
        "confidence": float(confidence),
        "reason": reason.strip(),
    }


def classify_problem(
    problem_statement: str,
    examples: Optional[str] = None,
    constraints: Optional[str] = None,
) -> dict:
    if not problem_statement or not problem_statement.strip():
        raise ValueError("problem_statement must be a non-empty string.")

    prompt = _build_classifier_prompt(
        problem_statement=problem_statement,
        examples=examples,
        constraints=constraints,
    )

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=MAX_CLASSIFIER_TOKENS,
        temperature=CLASSIFIER_TEMPERATURE,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    raw_text = response.content[0].text.strip()
    return _safe_parse_classifier_output(raw_text)