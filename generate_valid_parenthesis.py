'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def genParenHelper(self, parenthesis, openCount: int, closeCount: int, result: List[str]):
        if openCount == 0 and closeCount == 0:
            result.append(parenthesis)
        if closeCount > openCount:
            self.genParenHelper(parenthesis + ")", openCount, closeCount - 1, result)
        if openCount>0:
            self.genParenHelper(parenthesis + "(", openCount - 1, closeCount, result)
        
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.genParenHelper("(", n-1, n, result)
        return result
        