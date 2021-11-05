# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sumOfLeftLeavesCalc(root, False)
    def sumOfLeftLeavesCalc(self, root: Optional[TreeNode], left: bool) -> int:
        if root == None:
            return 0
        return (root.val if (left and (not root.left) and (not root.right)) else 0) +\
                self.sumOfLeftLeavesCalc(root.left, True) +\
                self.sumOfLeftLeavesCalc(root.right, False)
