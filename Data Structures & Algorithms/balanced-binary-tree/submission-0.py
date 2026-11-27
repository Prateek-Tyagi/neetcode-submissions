# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.Balanced = True

        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            h_diff = left_height - right_height

            if abs(h_diff) >= 2:
                self.Balanced = False
            return 1 + max(left_height, right_height)
            
        dfs(root)

        return self.Balanced
        