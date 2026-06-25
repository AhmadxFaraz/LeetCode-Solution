# Approach 1
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using brute force approach to find the two numbers.
        for i in range(len(nums)):
            if i<len(nums)-1:
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        return [i, j] # Assuming each input would have exactly one solution.

# Approach 2
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using hash map to find the two numbers.
        pass # To be implemented. Once I learn how to use hash map in python, I will implement this approach. 