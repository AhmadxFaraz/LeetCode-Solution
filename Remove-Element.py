# Solution to problem 27: Remove Element on LeetCode.
# Approach 1:
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        arr = []
        count = 0
        k = 0
        for n in nums:
            if n!=val:
                arr.append(n)
                k+=1
            else:
                count+=1
        for _ in range(count):
            arr.append('_')
        
        nums[:] = arr
        return k
        
# Results - Accepted
# Method Used in python, new list containing all the elements except the target value is created. 
# And number of number of times target value is found is counted. 