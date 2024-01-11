# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = -1
        def recur(root):
            nonlocal ans
            if root.left is None and root.right is None:
                return root.val, root.val
            a, b = root.val, root.val

            if root.left:
                t1, t2 = recur(root.left)
                a = max(t1, a)
                b = min(t2, b)
                ans = max(ans, abs(root.val - t1), abs(root.val - t2))
            
            if root.right:
                t1, t2 = recur(root.right)
                a = max(t1, a)
                b = min(t2, b)
                ans = max(ans, abs(root.val - t1), abs(root.val - t2))
            return a, b
        recur(root)
        return ans
