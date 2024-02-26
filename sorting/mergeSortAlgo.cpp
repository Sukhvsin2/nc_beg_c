class Solution {
    void merge(vector<int> &left, vector<int> &right, vector<int> &nums){
        int i = 0, j = 0, k = 0;

        while(i < left.size() && j < right.size()){
            if(left[i] <= right[j]){
                nums[k] = left[i];
                i++;
            }
            else{
                nums[k] = right[j];
                j++;
            }
            k++;
        }

        while(i < left.size()){
            nums[k] = left[i];
            i++; k++;
        }

        while(j < right.size()){
            nums[k] = right[j];
            j++; k++;
        }
    }

    void mergeSort(vector<int> &nums){
        if(nums.size() < 2) return;
        int numsLen = nums.size();
        vector<int> left, right;
        int mid = numsLen/2;
        for(int i=0;i<numsLen;i++){
            if(i<mid)
                left.push_back(nums[i]);
            else
                right.push_back(nums[i]);
        }

        mergeSort(left);
        mergeSort(right);

        merge(left, right, nums);
    }

public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums);
        return nums;
    }
};
