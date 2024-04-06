"""
Submitted: October 14, 2022
Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
           
        
        for i in range (len(nums)):
            leftover = target - nums[i]     #Target - the number will result in the other half of the sum
            
            for j in range(i+1, len(nums)):
                if nums[j] == leftover:     #if the other half of the sum is found, the pair is complete! :)
                    return [i, j]
