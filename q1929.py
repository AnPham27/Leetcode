"""
Submitted: April 18, 2024
Question: Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed). 
Specifically, ans is the concatenation of two nums arrays.
"""

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for n in range(len(nums)):
            ans.append(nums[n])

        for n in range(len(nums)):
            ans.append(nums[n])
        
        return ans