"""
Submitted: October 14, 2022
2307ms
Beats 21.44% of users with Python
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
