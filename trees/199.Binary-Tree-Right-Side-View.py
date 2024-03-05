# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []

        q = deque()

        if root:
            res.append(root.val)
            q.append(root)

        while len(q) > 0:
            temp: List[int] = []

            for i in range(len(q)):
                curr: TreeNode = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    temp.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    temp.append(curr.right)
            if temp:
                res.append(temp[-1].val)
        
        return res
