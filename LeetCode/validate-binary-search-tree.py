# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)

    def dfs(
        self, root: Optional[TreeNode], max_left=float("-inf"), min_right=float("inf")
    ) -> bool:
        if root is None:
            return True

        if not (max_left < root.val < min_right):
            return False

        return self.dfs(root.left, max_left=max_left, min_right=root.val) and self.dfs(
            root.right, max_left=root.val, min_right=min_right
        )
