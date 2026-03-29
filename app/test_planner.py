from agent.classifier import classify_problem
from agent.retriever import get_pattern_details
from agent.planner import generate_plan

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

classification = classify_problem(problem, examples, constraints)
pattern_info = get_pattern_details(classification["pattern"])

plan = generate_plan(problem, pattern_info, examples, constraints)

print("Pattern:", classification)
print("\nPlan:\n", plan)