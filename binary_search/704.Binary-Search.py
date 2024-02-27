class Solution:
    def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> int:
        mid = (left+right)//2

        while left <= right:
            if target < nums[mid]:
                return self.binarySearch(nums, left, mid-1, target)
            elif target > nums[mid]:
                return self.binarySearch(nums, mid+1, right, target)
            else:
                return mid

        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        return self.binarySearch(nums, left, right, target)

'''
class Solution {
    int binarySearch(vector<int> & nums, int left, int right, int target){
        int mid = (left+right)/2;

        while(left<=right){
            if(nums[mid] == target) return mid;
            else if(target < nums[mid]) return binarySearch(nums, left, mid-1, target);
            else return binarySearch(nums, mid+1, right, target);
        }
        return -1;
    }

public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size()-1, target);
    }
};
'''
