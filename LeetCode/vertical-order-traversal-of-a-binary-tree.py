from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        treeMap = defaultdict(list)
        treeDeque = deque()
        treeDeque.append((root, 0, 0))

        while len(treeDeque) != 0:
            node, row, col = treeDeque.popleft()
            treeMap[col].append((row, node.val))

            if node.left:
                treeDeque.append((node.left, row + 1, col - 1))

            if node.right:
                treeDeque.append((node.right, row + 1, col + 1))

        return [[i[1] for i in sorted(v)] for k, v in sorted(treeMap.items())]
