from agent.classifier import classify_problem
from agent.retriever import get_pattern_details
from agent.planner import generate_plan
from agent.coder import generate_code
from agent.tester import evaluate_code

problem = """
Given an array of integers nums and an integer k, return the maximum sum of any contiguous subarray of size k.
"""

examples = """
Input: nums = [2,1,5,1,3,2], k = 3
Output: 9
"""

constraints = """
1 <= len(nums) <= 10^5
"""

test_cases = [
    {"input": ([2,1,5,1,3,2], 3), "output": 9},
    {"input": ([1,2,3,4,5], 2), "output": 9},
    {"input": ([5,5,5,5], 1), "output": 5},
]

classification = classify_problem(problem, examples, constraints)
pattern_info = get_pattern_details(classification["pattern"])
plan = generate_plan(problem, pattern_info, examples, constraints)
code_result = generate_code(problem, pattern_info, plan, examples, constraints)

evaluation = evaluate_code(code_result["code"], test_cases)

print("\nGenerated Code:\n")
print(code_result["code"])

print("\nEvaluation Result:\n")
print(evaluation)