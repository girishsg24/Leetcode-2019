'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        parentDict = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        for paren in s:
            if paren in parentDict.values():
                stack.append(paren)
            elif len(stack)>0 and parentDict[paren] == stack[-1]:
                    stack.pop()
            else:
                return False
        if len(stack)>0:
            return False
        return True
        