# Solution to problem number 724 on LeetCode: Find Pivot Index
# Method used: Brute Force, it exceeds time limit, not accepted by LeetCode
class Solution:
    def pivotIndex(self, nums):
        n = len(nums)
        for i in range(n):
            left_sum = 0
            right_sum = 0
            if i!=0:
                for j in range(0,i):
                    left_sum+=nums[j]
            if i!=n-1:
                for j in range(n-1,i,-1):
                    right_sum+=nums[j]
            if left_sum==right_sum:
                return i
        return -1

# Method used: Prefix Sum, it is accepted by LeetCode
class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == (total_sum - left_sum - nums[i]):
                return i
            left_sum += nums[i]
        return -1
            

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(solution.pivotIndex(nums))  # Output: 3