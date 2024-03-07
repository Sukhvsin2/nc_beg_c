class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countNums = {}
        index = 0
        for i in nums:
            diff = target - i
            if diff in countNums:
                return [countNums[diff], index]
            else:
                countNums[i] = index
            index += 1
