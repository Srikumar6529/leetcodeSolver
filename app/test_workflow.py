from agent.workflow import run_agent

problem = """
Given a string s, find the length of the longest substring without repeating characters.
"""

examples = """
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""

constraints = """
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

test_cases = [
    {"input": ("abcabcbb",), "output": 3},
    {"input": ("bbbbb",), "output": 1},
    {"input": ("pwwkew",), "output": 3},
    {"input": ("",), "output": 0},
    {"input": ("dvdf",), "output": 3},
]

result = run_agent(problem, examples, constraints, test_cases)
print(result)