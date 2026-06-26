# Solution to Leetcode problem 4: Median of Two Sorted Arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Approach 1: Merging the two arrays and sorting them to find the median.
        y = 5
        m = len(nums1)
        n = len(nums2)
        new_arr = nums1 + nums2 # Merging the two arrays into one array.
        new_arr.sort() # Sorting the merged array.
        x = m+n
        if x%2!=0:
            x = (x//2) # find the middle index of the merged array.
            num = float(new_arr[x])  # saving the middlemost number.
            return num
        else:
            x = (x//2) 
            num = (new_arr[x-1] + new_arr[x]) / 2.0 # finding the average of the two middlemost numbers.
            return num

        # Approach 2, to be added soon.