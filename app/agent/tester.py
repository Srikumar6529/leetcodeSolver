import traceback
from typing import List, Dict, Any


def run_code(code: str) -> dict:
    local_env = {}

    try:
        exec(code, {}, local_env)
    except Exception as e:
        return {
            "success": False,
            "error": f"Execution error:\n{traceback.format_exc()}"
        }

    if "solve" not in local_env:
        return {
            "success": False,
            "error": "No function named 'solve' found in generated code"
        }

    return {
        "success": True,
        "function": local_env["solve"]
    }


def run_tests(func, test_cases: List[Dict[str, Any]]) -> dict:
    results = []

    for i, test in enumerate(test_cases):
        try:
            output = func(*test["input"])
            expected = test["output"]

            passed = output == expected

            results.append({
                "test_id": i,
                "input": test["input"],
                "expected": expected,
                "actual": output,
                "passed": passed
            })

        except Exception as e:
            results.append({
                "test_id": i,
                "input": test["input"],
                "expected": test["output"],
                "actual": str(e),
                "passed": False,
                "error": traceback.format_exc()
            })

    all_passed = all(r["passed"] for r in results)

    return {
        "all_passed": all_passed,
        "results": results
    }


def evaluate_code(code: str, test_cases: List[Dict[str, Any]]) -> dict:
    exec_result = run_code(code)

    if not exec_result["success"]:
        return {
            "success": False,
            "stage": "execution",
            "error": exec_result["error"]
        }

    func = exec_result["function"]
    test_result = run_tests(func, test_cases)

    return {
        "success": test_result["all_passed"],
        "stage": "testing",
        "details": test_result
    }