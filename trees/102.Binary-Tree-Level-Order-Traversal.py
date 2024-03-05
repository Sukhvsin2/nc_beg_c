# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res: List[List[int]] = []
        level: int = 0
        if root:
            q.append(root)

        while len(q) > 0:
            tempList: List[int] = []
            for i in range(len(q)):
                curr = q.popleft()
                tempList.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(tempList)
            level += 1
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
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        vector<vector<int>> res;
        if(root != NULL)
            q.push(root);
        
        while(q.size() > 0){
            vector<int> temp;
            int s = q.size();
            for(int i=0;i<s;i++){
                TreeNode* curr = q.front();
                q.pop();
                temp.push_back(curr->val);

                if(curr->left != NULL) q.push(curr->left);
                if(curr->right != NULL) q.push(curr->right);
            }
            res.push_back(temp);
        }

        return res;
    }
};
'''
