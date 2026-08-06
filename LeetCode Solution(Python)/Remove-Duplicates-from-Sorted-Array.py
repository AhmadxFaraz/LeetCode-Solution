# Solution to problem 26: Remove Duplicates from Sorted Array on LeetCode.
# Approach 1:

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        opt = set(nums)
        new_arr = list(opt)
        new_arr.sort()
        nums[:] = new_arr
        y = len(nums)
        return y

# Results - Accepted
# Method Used in python, new list containing all the unique elements is created.