# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return 

        ### Post order Traversal ###
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root


"""
[1] + [3] + [6] + [7] + [2] + [5] + [4]
invertTree(3): 
invertTree(2): 
"""
        