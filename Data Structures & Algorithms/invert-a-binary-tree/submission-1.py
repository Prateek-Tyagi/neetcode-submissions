# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)

        
        
        # def dfs(node):
        #     if not node:
        #         return
        #     right_subtree = node.right
        #     node.right = node.left
        #     node.left = right_subtree

        #     dfs(node.left)
        #     dfs(node.right)
        
        # dfs(root)

        return root