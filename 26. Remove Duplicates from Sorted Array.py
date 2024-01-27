class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                nums[count+1] = nums[i]
                count = count + 1
        
        return count+1
        
