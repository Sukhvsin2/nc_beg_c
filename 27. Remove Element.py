class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count = count + 1

        print(nums)
        return count

  """
  C++ Solution
  
  class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            int index = 0;
            for(int i=0;i<nums.size();i++){
                if(nums[i] != val){
                    nums[index] = nums[i];
                    index++;
                }
            }
            return index;
        }
    };
    
    /**
    Test Case:
    [2,2,2,3] 3
    
    index = [2] -> 2
    nums[i] = [3] -> 3

    **/ 
  """
