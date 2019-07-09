'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    def __init__(self):
        self.phoneMap = {
            "2":["a","b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

    def letterCombinations(self, digits):
        result = []
        def getLetterCombinations(currentStr, digits):
            if len(digits) == 0:
                return result.append(currentStr)
            for curChar in self.phoneMap[digits[0]]:
                getLetterCombinations(currentStr+curChar, digits[1:])
        
        if len(digits)>0:
            getLetterCombinations("", digits)
                
        return result