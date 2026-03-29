from agent.workflow import run_agent


PROBLEMS = [
    {
        "name": "Minimum Window Substring",
        "expected_pattern": "sliding_window",
        "problem": """
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t, including duplicates, is included in the window. If there is no such substring, return an empty string.
""",
        "examples": """
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""
""",
        "constraints": """
1 <= len(s), len(t) <= 10^5
s and t consist of English letters
""",
        "test_cases": [
            {"input": ("ADOBECODEBANC", "ABC"), "output": "BANC"},
            {"input": ("a", "a"), "output": "a"},
            {"input": ("a", "aa"), "output": ""},
            {"input": ("aa", "aa"), "output": "aa"},
            {"input": ("ab", "b"), "output": "b"},
        ],
    },
    {
        "name": "Word Break",
        "expected_pattern": "dynamic_programming",
        "problem": """
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
""",
        "examples": """
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
""",
        "constraints": """
1 <= len(s) <= 300
1 <= len(wordDict) <= 1000
1 <= len(wordDict[i]) <= 20
""",
        "test_cases": [
            {"input": ("leetcode", ["leet", "code"]), "output": True},
            {"input": ("applepenapple", ["apple", "pen"]), "output": True},
            {"input": ("catsandog", ["cats", "dog", "sand", "and", "cat"]), "output": False},
            {"input": ("aaaaaaa", ["aaaa", "aaa"]), "output": True},
            {"input": ("cars", ["car", "ca", "rs"]), "output": True},
        ],
    },
    {
        "name": "Coin Change II",
        "expected_pattern": "dynamic_programming",
        "problem": """
You are given an integer amount and an array coins representing coins of different denominations. Return the number of combinations that make up that amount.

You may assume that you have an infinite number of each kind of coin.
""",
        "examples": """
Input: amount = 5, coins = [1,2,5]
Output: 4

Input: amount = 3, coins = [2]
Output: 0

Input: amount = 10, coins = [10]
Output: 1
""",
        "constraints": """
0 <= amount <= 5000
1 <= len(coins) <= 300
1 <= coins[i] <= 5000
All the values of coins are unique
""",
        "test_cases": [
            {"input": (5, [1, 2, 5]), "output": 4},
            {"input": (3, [2]), "output": 0},
            {"input": (10, [10]), "output": 1},
            {"input": (0, [1, 2, 5]), "output": 1},
            {"input": (4, [1, 2, 3]), "output": 4},
        ],
    },
    {
        "name": "Daily Temperatures",
        "expected_pattern": "stack",
        "problem": """
Given an array of integers temperatures representing the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the i-th day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
""",
        "examples": """
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]
""",
        "constraints": """
1 <= len(temperatures) <= 10^5
30 <= temperatures[i] <= 100
""",
        "test_cases": [
            {"input": ([73, 74, 75, 71, 69, 72, 76, 73],), "output": [1, 1, 4, 2, 1, 1, 0, 0]},
            {"input": ([30, 40, 50, 60],), "output": [1, 1, 1, 0]},
            {"input": ([30, 60, 90],), "output": [1, 1, 0]},
            {"input": ([90, 80, 70],), "output": [0, 0, 0]},
        ],
    },
    {
        "name": "Rotting Oranges",
        "expected_pattern": "graph",
        "problem": """
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange,
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
""",
        "examples": """
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Input: grid = [[0,2]]
Output: 0
""",
        "constraints": """
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2
""",
        "test_cases": [
            {"input": ([[2, 1, 1], [1, 1, 0], [0, 1, 1]],), "output": 4},
            {"input": ([[2, 1, 1], [0, 1, 1], [1, 0, 1]],), "output": -1},
            {"input": ([[0, 2]],), "output": 0},
            {"input": ([[1]],), "output": -1},
        ],
    },
    {
        "name": "Top K Frequent Elements",
        "expected_pattern": "heap_priority_queue",
        "problem": """
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
""",
        "examples": """
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
""",
        "constraints": """
1 <= len(nums) <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= number of unique elements in nums
""",
        "test_cases": [
            {"input": ([1, 1, 1, 2, 2, 3], 2), "output": [1, 2]},
            {"input": ([1], 1), "output": [1]},
            {"input": ([4, 4, 4, 6, 6, 7], 1), "output": [4]},
        ],
    },
    {
        "name": "Combination Sum",
        "expected_pattern": "backtracking",
        "problem": """
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
""",
        "examples": """
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
""",
        "constraints": """
1 <= len(candidates) <= 30
1 <= candidates[i] <= 40
All elements of candidates are distinct
1 <= target <= 40
""",
        "test_cases": [
            {"input": ([2, 3, 6, 7], 7), "output": [[2, 2, 3], [7]]},
            {"input": ([2, 3, 5], 8), "output": [[2, 2, 2, 2], [2, 3, 3], [3, 5]]},
            {"input": ([2], 1), "output": []},
        ],
    },
    {
        "name": "Kth Smallest Element in a BST",
        "expected_pattern": "tree",
        "problem": """
Given the root of a binary search tree and an integer k, return the kth smallest value in the tree.
""",
        "examples": """
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
""",
        "constraints": """
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
""",
        "test_cases": [
            {"input": ([3, 1, 4, None, 2], 1), "output": 1},
            {"input": ([5, 3, 6, 2, 4, None, None, 1], 3), "output": 3},
        ],
    },
]


def normalize(value):
    if isinstance(value, tuple):
        return [normalize(v) for v in value]
    if isinstance(value, list):
        return [normalize(v) for v in value]
    return value


def normalize_nested_unordered_list(value):
    if isinstance(value, list):
        if all(not isinstance(x, list) for x in value):
            return sorted(value)
        return sorted([normalize_nested_unordered_list(x) for x in value])
    return value


def outputs_match(actual, expected, problem_name):
    actual = normalize(actual)
    expected = normalize(expected)

    if problem_name == "Top K Frequent Elements":
        return sorted(actual) == sorted(expected)

    if problem_name == "Combination Sum":
        actual_norm = sorted([sorted(x) for x in actual])
        expected_norm = sorted([sorted(x) for x in expected])
        return actual_norm == expected_norm

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
    print("HARD BENCHMARK SUMMARY")
    print(f"Total Problems: {total_problems}")
    print(f"Successful Workflows: {successful_workflows}/{total_problems}")
    print(f"Correct Pattern Predictions: {correct_patterns}/{total_problems}")
    print(f"Problems Passing All Tests: {fully_passed_problems}/{total_problems}")
    print("#" * 100)


if __name__ == "__main__":
    run_benchmark()