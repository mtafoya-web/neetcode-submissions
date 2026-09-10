# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        def dfs(root, order):
            if not root: return order 

            dfs(root.left, order)
            order.append(root.val)
            dfs(root.right, order)

            return order
        return dfs(root, traversal)
        