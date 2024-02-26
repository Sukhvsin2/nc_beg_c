class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while(j >= 0 and nums[j] > key):
                # swap values
                # temp = nums[j]
                nums[j+1] = nums[j]
                # nums[j+1] = temp
                j -= 1
            nums[j+1] = key
        
        return nums
        
