import json
import re


def extract_json_text(raw_text: str) -> str:
    text = raw_text.strip()

    # Case 1: fenced markdown block
    fenced_match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.DOTALL)
    if fenced_match:
        return fenced_match.group(1).strip()

    # Case 2: raw JSON object somewhere in the text
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and start < end:
        return text[start:end + 1].strip()

    return text


def parse_json_response(raw_text: str) -> dict:
    cleaned = extract_json_text(raw_text)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Model returned invalid JSON.\nRaw output:\n{raw_text}\n\nCleaned output:\n{cleaned}"
        ) from exc