# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkPath(self, root: Optional[TreeNode], countSum: int, tSum: int) -> bool:
        if not root:
            return False
        
        countSum += root.val
        if not root.left and not root.right:
            return countSum == tSum

        return (self.checkPath(root.left, countSum, tSum) or self.checkPath(root.right, countSum, tSum))
        


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.checkPath(root, 0, targetSum)
