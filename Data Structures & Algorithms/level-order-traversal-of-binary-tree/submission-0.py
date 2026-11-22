# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = deque([root])
        result = []
        while d:
            l = len(d)
            res_child = []
            while l > 0:
                curr = d.popleft()
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
                res_child.append(curr.val)
                l -= 1
            result.append(res_child[:])
        return result