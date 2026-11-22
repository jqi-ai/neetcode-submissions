# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        d = deque([root])
        result = []
        while d:
            len_d = len(d)
            right = None
            while len_d > 0:
                curr = d.popleft()
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
                right = curr
                len_d -= 1
            result.append(right.val)
        return result