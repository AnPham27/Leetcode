"""
Submitted: April 18, 2024
Question: You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
Return the score of s.
"""

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum = 0
        temp = ord(s[0])

        for letter in s[1:]:
            sum += abs(temp - ord(letter))
            temp = ord(letter)
    
        return sum
       