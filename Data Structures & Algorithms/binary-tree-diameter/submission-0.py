# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if root is None:
                return 0, 0

            left_height, left_diameter = dfs(root.left)
            right_height, right_diameter = dfs(root.right)

            height = 1 + max(left_height, right_height)

            root_diam = left_height + right_height

            diameter = max(
                root_diam,
                left_diameter,
                right_diameter
            )

            return height, diameter

        height, diameter = dfs(root)
        return diameter

        