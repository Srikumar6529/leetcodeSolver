import json
from anthropic import Anthropic

from app.config import ANTHROPIC_API_KEY, CLAUDE_MODEL

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def generate_code(
    problem: str,
    pattern_info: dict,
    plan: dict,
    examples: str = "",
    constraints: str = "",
) -> dict:
    prompt = f"""
You are an expert Python coding assistant.

Your task is to write a correct Python solution for the given algorithm problem.

Problem:
{problem}

Pattern selected:
{pattern_info["display_name"]}

Pattern guidance:
{pattern_info["use_when"]}

Pattern template:
{pattern_info["template"]}

Planned approach:
{plan["approach"]}

Pseudocode:
{plan["pseudocode"]}

Edge cases:
{json.dumps(plan["edge_cases"], indent=2)}

Examples:
{examples if examples else "Not provided"}

Constraints:
{constraints if constraints else "Not provided"}

Instructions:
- Write Python code only for the solution
- The function name must be exactly: solve
- Include only the function definition and its logic
- Do not include markdown fences
- Do not include explanations outside JSON
- Return valid JSON only

Return JSON in this format:
{{
  "code": "def solve(...):\\n    ..."
}}
"""

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=700,
        temperature=0.1,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    raw = response.content[0].text.strip()

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Coder returned invalid JSON:\n{raw}") from exc

    if not isinstance(parsed, dict) or "code" not in parsed:
        raise ValueError(f"Coder output missing 'code' field:\n{raw}")

    code = parsed["code"]
    if not isinstance(code, str) or "def solve" not in code:
        raise ValueError(f"Generated code does not contain required solve function:\n{code}")

    return {"code": code.strip()}