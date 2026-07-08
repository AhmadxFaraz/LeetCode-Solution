# Solution to problem 283: Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = len(nums)
        result = []
        count = 0
        for i in range(x):
            if nums[i]!=0:
                result.append(nums[i])
            else:
                count+=1
        result.extend([0]*count)
        nums[:] = result

if __name__ == "__main__":
    nums = [0,1,0,3,12,0,0,4,18,9]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)