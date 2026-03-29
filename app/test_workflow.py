from agent.workflow import run_agent

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

result = run_agent(problem, examples, constraints, test_cases)

print(result)