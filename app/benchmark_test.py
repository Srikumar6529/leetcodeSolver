from agent.workflow import run_agent


PROBLEMS = [
    {
        "name": "Maximum Sum Subarray of Size K",
        "expected_pattern": "sliding_window",
        "problem": """
Given an array of integers nums and an integer k, return the maximum sum of any contiguous subarray of size k.
""",
        "examples": """
Input: nums = [2,1,5,1,3,2], k = 3
Output: 9

Input: nums = [1,2,3,4,5], k = 2
Output: 9
""",
        "constraints": """
1 <= len(nums) <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= len(nums)
""",
        "test_cases": [
            {"input": ([2, 1, 5, 1, 3, 2], 3), "output": 9},
            {"input": ([1, 2, 3, 4, 5], 2), "output": 9},
            {"input": ([5, 5, 5, 5], 1), "output": 5},
            {"input": ([-1, -2, -3, -4], 2), "output": -3},
        ],
    },
    {
        "name": "Two Sum",
        "expected_pattern": "hash_map",
        "problem": """
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

Return the answer in any order.
""",
        "examples": """
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]
""",
        "constraints": """
2 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
""",
        "test_cases": [
            {"input": ([2, 7, 11, 15], 9), "output": [0, 1]},
            {"input": ([3, 2, 4], 6), "output": [1, 2]},
            {"input": ([3, 3], 6), "output": [0, 1]},
        ],
    },
    {
        "name": "Valid Parentheses",
        "expected_pattern": "stack",
        "problem": """
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

A string is valid if:
- open brackets are closed by the same type of brackets
- open brackets are closed in the correct order
- every close bracket has a corresponding open bracket
""",
        "examples": """
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False
""",
        "constraints": """
1 <= len(s) <= 10^4
s consists only of parentheses characters
""",
        "test_cases": [
            {"input": ("()",), "output": True},
            {"input": ("()[]{}",), "output": True},
            {"input": ("(]",), "output": False},
            {"input": ("([)]",), "output": False},
            {"input": ("{[]}",), "output": True},
        ],
    },
    {
        "name": "Binary Search",
        "expected_pattern": "binary_search",
        "problem": """
Given a sorted array of integers nums and an integer target, return the index of target if it exists, otherwise return -1.
""",
        "examples": """
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
""",
        "constraints": """
1 <= len(nums) <= 10^4
nums is sorted in ascending order
all elements are unique
""",
        "test_cases": [
            {"input": ([-1, 0, 3, 5, 9, 12], 9), "output": 4},
            {"input": ([-1, 0, 3, 5, 9, 12], 2), "output": -1},
            {"input": ([5], 5), "output": 0},
            {"input": ([5], -5), "output": -1},
        ],
    },
    {
        "name": "Longest Substring Without Repeating Characters",
        "expected_pattern": "sliding_window",
        "problem": """
Given a string s, find the length of the longest substring without repeating characters.
""",
        "examples": """
Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3
""",
        "constraints": """
0 <= len(s) <= 5 * 10^4
s consists of English letters, digits, symbols, and spaces
""",
        "test_cases": [
            {"input": ("abcabcbb",), "output": 3},
            {"input": ("bbbbb",), "output": 1},
            {"input": ("pwwkew",), "output": 3},
            {"input": ("",), "output": 0},
            {"input": ("dvdf",), "output": 3},
        ],
    },
    {
        "name": "Product of Array Except Self",
        "expected_pattern": "arrays",
        "problem": """
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Do not use division.
""",
        "examples": """
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
""",
        "constraints": """
2 <= len(nums) <= 10^5
-30 <= nums[i] <= 30
""",
        "test_cases": [
            {"input": ([1, 2, 3, 4],), "output": [24, 12, 8, 6]},
            {"input": ([-1, 1, 0, -3, 3],), "output": [0, 0, 9, 0, 0]},
            {"input": ([2, 3],), "output": [3, 2]},
        ],
    },
    {
        "name": "Number of Islands",
        "expected_pattern": "graph",
        "problem": """
Given an m x n 2D grid of characters '1' and '0', return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically.
""",
        "examples": """
Input:
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input:
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
""",
        "constraints": """
1 <= m, n <= 300
""",
        "test_cases": [
            {
                "input": ([["1", "1", "1", "1", "0"],
                           ["1", "1", "0", "1", "0"],
                           ["1", "1", "0", "0", "0"],
                           ["0", "0", "0", "0", "0"]],),
                "output": 1,
            },
            {
                "input": ([["1", "1", "0", "0", "0"],
                           ["1", "1", "0", "0", "0"],
                           ["0", "0", "1", "0", "0"],
                           ["0", "0", "0", "1", "1"]],),
                "output": 3,
            },
        ],
    },
    {
        "name": "Coin Change",
        "expected_pattern": "dynamic_programming",
        "problem": """
You are given an integer array coins representing coins of different denominations and an integer amount.

Return the fewest number of coins needed to make up that amount. If that amount cannot be made up, return -1.
""",
        "examples": """
Input: coins = [1,2,5], amount = 11
Output: 3

Input: coins = [2], amount = 3
Output: -1
""",
        "constraints": """
1 <= len(coins) <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
""",
        "test_cases": [
            {"input": ([1, 2, 5], 11), "output": 3},
            {"input": ([2], 3), "output": -1},
            {"input": ([1], 0), "output": 0},
            {"input": ([1], 1), "output": 1},
        ],
    },
]


def normalize_output(value):
    if isinstance(value, tuple):
        return list(value)
    return value


def outputs_match(actual, expected, problem_name):
    actual = normalize_output(actual)
    expected = normalize_output(expected)

    if problem_name == "Two Sum":
        if isinstance(actual, list) and isinstance(expected, list):
            return sorted(actual) == sorted(expected)
    return actual == expected


def count_passed_tests(evaluation_details, problem_name):
    results = evaluation_details.get("results", [])
    passed = 0

    for item in results:
        actual = item.get("actual")
        expected = item.get("expected")

        if outputs_match(actual, expected, problem_name):
            passed += 1

    return passed, len(results)


def print_problem_summary(problem_name, result, expected_pattern):
    print("=" * 100)
    print(f"Problem: {problem_name}")
    print(f"Expected Pattern: {expected_pattern}")

    if not result.get("success"):
        print("Workflow Status: FAILED")
        print(f"Attempts: {result.get('attempts')}")
        print(f"Predicted Pattern: {result.get('pattern', {}).get('pattern', 'N/A')}")
        print(f"Evaluation: {result.get('evaluation')}")
        return

    predicted_pattern = result["pattern"]["pattern"]
    attempts = result["attempts"]
    evaluation = result["evaluation"]
    details = evaluation.get("details", {})

    passed_tests, total_tests = count_passed_tests(details, problem_name)
    pattern_match = predicted_pattern == expected_pattern

    print("Workflow Status: SUCCESS")
    print(f"Predicted Pattern: {predicted_pattern}")
    print(f"Pattern Correct: {pattern_match}")
    print(f"Attempts Used: {attempts}")
    print(f"Tests Passed: {passed_tests}/{total_tests}")

    if not pattern_match:
        print(f"Pattern Reason: {result['pattern'].get('reason')}")

    if passed_tests != total_tests:
        print("Failed Tests:")
        for item in details.get("results", []):
            if not outputs_match(item.get("actual"), item.get("expected"), problem_name):
                print(
                    f"  Test {item.get('test_id')}: expected={item.get('expected')} actual={item.get('actual')}"
                )


def run_benchmark():
    total_problems = len(PROBLEMS)
    successful_workflows = 0
    correct_patterns = 0
    fully_passed_problems = 0

    for problem in PROBLEMS:
        try:
            result = run_agent(
                problem=problem["problem"],
                examples=problem["examples"],
                constraints=problem["constraints"],
                test_cases=problem["test_cases"],
            )

            print_problem_summary(
                problem_name=problem["name"],
                result=result,
                expected_pattern=problem["expected_pattern"],
            )

            if result.get("success"):
                successful_workflows += 1

                predicted_pattern = result["pattern"]["pattern"]
                if predicted_pattern == problem["expected_pattern"]:
                    correct_patterns += 1

                passed_tests, total_tests = count_passed_tests(
                    result["evaluation"].get("details", {}),
                    problem["name"],
                )
                if passed_tests == total_tests:
                    fully_passed_problems += 1

        except Exception as exc:
            print("=" * 100)
            print(f"Problem: {problem['name']}")
            print("Workflow Status: CRASHED")
            print(f"Error: {exc}")

    print("\n" + "#" * 100)
    print("BENCHMARK SUMMARY")
    print(f"Total Problems: {total_problems}")
    print(f"Successful Workflows: {successful_workflows}/{total_problems}")
    print(f"Correct Pattern Predictions: {correct_patterns}/{total_problems}")
    print(f"Problems Passing All Tests: {fully_passed_problems}/{total_problems}")
    print("#" * 100)


if __name__ == "__main__":
    run_benchmark()