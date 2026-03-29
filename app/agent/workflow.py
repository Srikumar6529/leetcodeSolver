from agent.classifier import classify_problem
from agent.retriever import get_pattern_details
from agent.planner import generate_plan
from agent.coder import generate_code
from agent.tester import evaluate_code

from anthropic import Anthropic
from config import ANTHROPIC_API_KEY, CLAUDE_MODEL

client = Anthropic(api_key=ANTHROPIC_API_KEY)


MAX_RETRIES = 2


def fix_code(problem, code, error_feedback):
    prompt = f"""
You are an expert Python developer.

The following code has errors or failed test cases.

Problem:
{problem}

Current Code:
{code}

Error / Test Feedback:
{error_feedback}

Fix the code so that it correctly solves the problem.

Rules:
- Keep function name: solve
- Return only corrected code
- No explanation
- Return JSON only

Format:
{{
  "code": "def solve(...): ..."
}}
"""

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=600,
        temperature=0.1,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    import json

    raw = response.content[0].text.strip()

    try:
        return json.loads(raw)["code"]
    except:
        raise ValueError(f"Fixer returned invalid JSON:\n{raw}")


def run_agent(problem, examples, constraints, test_cases):
    classification = classify_problem(problem, examples, constraints)
    pattern_info = get_pattern_details(classification["pattern"])
    plan = generate_plan(problem, pattern_info, examples, constraints)

    code_result = generate_code(problem, pattern_info, plan, examples, constraints)
    code = code_result["code"]

    attempt = 0

    while attempt <= MAX_RETRIES:
        evaluation = evaluate_code(code, test_cases)

        if evaluation["success"]:
            return {
                "success": True,
                "attempts": attempt + 1,
                "pattern": classification,
                "plan": plan,
                "code": code,
                "evaluation": evaluation
            }

        # if failed → fix code
        feedback = evaluation

        code = fix_code(problem, code, str(feedback))

        attempt += 1

    return {
        "success": False,
        "attempts": attempt,
        "pattern": classification,
        "plan": plan,
        "code": code,
        "evaluation": evaluation
    }