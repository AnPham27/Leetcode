"""
Submitted: April 2, 2024
Question: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        length = len(nums)

        for i in range(length):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
                  
        return index