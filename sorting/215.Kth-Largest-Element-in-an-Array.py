# This will not pass the final test case because of the time limitation of this algo
# need to solve the same problem with another algorithm(Heap)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, beg, end, k):
            pivot = end
            left = beg

            for i in range(beg, end):
                if nums[i] < nums[pivot]:
                    # swap
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
            # setting pivot val to the correct index
            nums[pivot], nums[left] = nums[left], nums[pivot]

            if left < len(nums) - k:
                # go right
                return quickSelect(nums, left+1, end, k)
            elif left > len(nums) - k:
                # go left
                return quickSelect(nums, beg, left-1, k)
            else:
                return nums[left]

        return quickSelect(nums, 0, len(nums)-1, k)
