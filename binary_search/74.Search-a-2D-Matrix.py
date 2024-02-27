class Solution:
    def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> bool:
        mid = (left+right) // 2

        while left <= right:
            if target < nums[mid]:
                return self.binarySearch(nums, left, mid-1, target)
            elif target > nums[mid]:
                return self.binarySearch(nums, mid+1, right, target)
            else:
                return True

        return False

    def searchRow(self, matrix: List[List[int]], left: int, right: int, target: int) -> bool:
        mid = (left + right) // 2

        while(left <= right):
            if target < matrix[mid][0]:
                return self.searchRow(matrix, left, mid-1, target)
            elif target > matrix[mid][-1]:
                return self.searchRow(matrix, mid+1, right, target)
            else:
                return self.binarySearch(matrix[mid], 0, len(matrix[mid])-1, target)

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchRow(matrix, 0, len(matrix)-1, target)
'''
class Solution {
    bool binarySearch(vector<int> &nums, int left, int right, int target){
        int mid = (left+right)/2;
        cout<<"Banry search called!\n";
        while(left <= right){
            cout<<"nums[mid]: "<<nums[mid]<<endl;
            if(target < nums[mid]) return binarySearch(nums, left, mid-1, target);
            if(target > nums[mid]) return binarySearch(nums, mid+1, right, target);
            else return true;
        }
        return false;
    }
    bool searchRow(vector<vector<int>>& matrix, int left, int right, int target){
        int mid = (left+right)/2;

        while(left <= right){
            cout<<"Matrix["<<mid<<"][0]: "<<matrix[mid][0]<<"-------"<<target<<endl;
            cout<<left<<"<="<<right<<endl;
            if(target < matrix[mid][0]) return searchRow(matrix, left, mid-1, target);
            else if(target > matrix[mid][matrix[mid].size()-1]) return searchRow(matrix, mid+1, right, target);
            else return binarySearch(matrix[mid], 0, matrix[mid].size()-1, target);
        }

        return false;
    }
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int left = 0, right = matrix.size()-1;
        return searchRow(matrix, left, right, target);
    }
};
'''
