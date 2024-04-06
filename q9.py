"""
Submitted: October 14, 2022
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        num = str(x)
        
        
        
        array = [] 
        
        #populate array with chars
        for char in num:
            array.append(char)
            
        print(array)
        
        #only check half the length and compare it 
        
        if x < 0:   #negative numbers are not palindrome
            return False
        
        else:
            for i in range (len(array)):
                if(array[i] != array[len(array)-i-1]):     #compares first char to last char then 
                    return False
        
        
        return True