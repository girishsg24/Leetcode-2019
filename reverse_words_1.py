'''
Given an input string, reverse the string word by word.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        return " ".join(wordList[::-1])
        