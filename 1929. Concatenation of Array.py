class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range((2* len(nums))):
            if(i > len(nums)-1):
                ans.append(nums[i - len(nums)])
                continue

            ans.append(nums[i])

        return ans

'''

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int size = nums.size();
        vector<int> ans;
        for(int i=0;i<(2*size);i++){
            if(i< size)
                ans.push_back(nums[i]);
            else
                ans.push_back(nums[i - size]);
        }
        return ans;
    }
};

'''
