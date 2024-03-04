# neetcode way
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        curr = root

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            k -= 1
            if k < 1:
                return curr.val
            curr = curr.right
        return curr.val

# my way
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root: Optional[TreeNode], arr: List[int], k: int):
        if not root:
            return

        self.traversal(root.left, arr, k)
        if len(arr) < k:
            arr.append(root.val)
        else:
            return
        self.traversal(root.right, arr, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.traversal(root, arr, k)
        return arr[k-1]
'''
