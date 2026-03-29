from agent.classifier import classify_problem

result = classify_problem(
    problem_statement="""
Given an array of integers nums and an integer k, return the maximum sum of any contiguous subarray of size k.
""",
    examples="""
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray [5,1,3] has maximum sum = 9
""",
    constraints="""
1 <= len(nums) <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= len(nums)
""",
)

print(result)