class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(left, right, nums):
            i, j, k = 0, 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                k += 1
                i += 1
            
            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1

            return nums
            
        def mergeSort(nums):
            if len(nums) < 2:
                return
            mid = len(nums)//2

            left, right = [], []

            for i in range(len(nums)):
                if i < mid:
                    left.append(nums[i])
                else:
                    right.append(nums[i])
            mergeSort(left)
            mergeSort(right)
            merge(left, right, nums)
            return nums
        
        return mergeSort(nums)
