# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def dfs(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val!=r.val:
                return False
            return dfs(l.left,r.right) and dfs(l.right,r.left)
        return dfs(root.left,root.right)
        