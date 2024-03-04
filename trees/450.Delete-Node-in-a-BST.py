# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        while root.left != None:
            root = root.left

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # TODO: Search for the node
        # TODO: case1: No Leaf
        #       case2: 1 child
        #       case3: 2 children

        if not root:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # found the key
            if root.left == None and root.right == None:
                root = None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                root.val = self.findMinNode(root.right, key).val
                root.right = self.deleteNode(root.right, root.val)

        return root

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
    TreeNode* findMinNode(TreeNode* root){
        while(root->left != NULL) root = root->left;
    	return root;
    }
public:
    TreeNode* deleteNode(TreeNode* root, int data) {
        
        // TODO: Search for the node

        // TODO: Delete the Node
            // Case1: Delete from the leaf
            // Case2: Delete with 1 child
                // - make child, root node. 
            // Case3: Delete with 2 children
                // - find min from right tree and make the root.
    if(root == NULL) return root;
        else if(data < root->val) root->left = deleteNode(root->left, data);
        else if(data > root->val) root->right = deleteNode(root->right, data);
        // found the element
        else{
            // case 1: No child - Leaf Node
            if(root->left == NULL && root->right == NULL) { 
    			delete root;
    			root = NULL;
    		}
    		//Case 2: One child 
    		else if(root->left == NULL) {
    			TreeNode *temp = root;
    			root = root->right;
    			delete temp;
    		}
    		else if(root->right == NULL) {
    			TreeNode *temp = root;
    			root = root->left;
    			delete temp;
    		}
    		// case 3: 2 children
    		else { 
    			TreeNode *temp = findMinNode(root->right);
    			root->val = temp->val;
    			root->right = deleteNode(root->right,temp->val);
    		}
        }
        return root;
    }
};
'''
