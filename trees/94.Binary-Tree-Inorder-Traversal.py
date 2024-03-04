# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root: Optional[TreeNode], res: List[int]) -> None:
        if not root:
            return
        
        self.traversal(root.left, res)
        res.append(root.val)
        self.traversal(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root, res)
        return res
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
    void traversal(TreeNode* root, vector<int> &arr){
        if(root == NULL) return;

        traversal(root->left, arr);
        arr.push_back(root->val);
        traversal(root->right, arr);
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> arr;
        traversal(root, arr);
        return arr;
    }
};
'''
