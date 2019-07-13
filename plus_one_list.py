'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if carry == 0:
                break
            newDigit = carry + digits[i]
            carry = newDigit // 10
            newDigit = newDigit % 10
            digits[i] = newDigit
        if carry > 0:
            digits.insert(0, carry)
        return digits