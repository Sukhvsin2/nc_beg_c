# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp: TreeNode = root
        if not temp:
            return None
        while temp:
            if temp.val == val:
                return temp
            elif val < temp.val:
                return self.searchBST(temp.left, val)
            else:
                return self.searchBST(temp.right, val)

        return temp

'''
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* temp = root;
        if(temp == NULL) return NULL;

        while(temp!=NULL){
            if(temp->val == val) return temp;
            else if(val < temp->val) return searchBST(temp->left, val);
            else return searchBST(temp->right, val);
        }
        return temp;
    }
};
'''
