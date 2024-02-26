class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def quickSort(nums, beg, end):
            if (end - beg+1) <= 1:
                return nums
            
            pivot = end
            left = beg

            for i in range(beg, end):
                if nums[i] < nums[pivot]:
                    nums[left], nums[i] = nums[i], nums[left]
                    left+=1

            nums[left], nums[pivot] = nums[pivot], nums[left]

            quickSort(nums, beg, left-1)
            quickSort(nums, left+1, end)
            return nums

        return quickSort(nums, 0, len(nums)-1)
