# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _diameterOfBinaryTree(self, root: Optional[TreeNode], count) -> int:
        if not root:
            return count
        
        left = self._diameterOfBinaryTree(root.left, count + 1)
        right = self._diameterOfBinaryTree(root.right, count + 1)
        return max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self._diameterOfBinaryTree(root, -1)