class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # implementation with hashmap
        countNums = {}
        for i in nums:
            if i not in countNums:
                countNums[i] = 1
            else:
                return True
        # print(countNums)
        return False

'''
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if(nums.size() < 2) return false;

        map<int, int> countInt;

        for(int i=0;i<nums.size();i++){
            if(countInt.find(nums[i])!= countInt.end()){
                return true;
            }
            else
                countInt[nums[i]] = 1;
        }

        return false;
    }
};
'''
