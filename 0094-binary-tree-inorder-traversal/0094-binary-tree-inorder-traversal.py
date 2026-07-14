# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        ans=[]
        def dfs(root):
            if root is None:
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans
        