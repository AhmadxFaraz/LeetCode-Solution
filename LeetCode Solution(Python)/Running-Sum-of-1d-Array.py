# Solution to LeetCode problem number 1480: Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            num = 0
            for j in range(0,i+1):
                num+=nums[j]
            result.append(num)
        return result