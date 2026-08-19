class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lis = set(nums)
        if(len(lis)!=len(nums)):
            return True
        else:
            return False
        