# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        def dfs(root):
            nonlocal cnt
            if not root:
                return None
            left = dfs(root.left)
            if left:
                return left
            cnt += 1
            if cnt == k:
                return root.val
            right = dfs(root.right)
            if right:
                return right
            return None
        return dfs(root)