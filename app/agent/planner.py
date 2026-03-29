from anthropic import Anthropic
from config import ANTHROPIC_API_KEY, CLAUDE_MODEL

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def generate_plan(problem: str, pattern_info: dict, examples: str = "", constraints: str = "") -> dict:
    prompt = f"""
You are an expert algorithm problem solver.

Your task is to create a clear solution plan before writing code.

Problem:
{problem}

Pattern to use:
{pattern_info['display_name']}

When to use this pattern:
{pattern_info['use_when']}

Template:
{pattern_info['template']}

Examples:
{examples if examples else "Not provided"}

Constraints:
{constraints if constraints else "Not provided"}

Instructions:
- First explain the approach clearly
- Then write pseudocode
- Then list important edge cases
- Keep everything concise and structured
- Do NOT write actual code

Return JSON only in this format:

{{
  "approach": "...",
  "pseudocode": "...",
  "edge_cases": ["...", "..."]
}}
"""

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=500,
        temperature=0.2,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    raw = response.content[0].text.strip()

    import json
    try:
        return json.loads(raw)
    except:
        raise ValueError(f"Planner returned invalid JSON:\n{raw}")