# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _isBalanced(self, root: Optional[TreeNode], index: int) -> int:
        if not root:
            return index

        left = self._isBalanced(root.left, index + 1)
        right = self._isBalanced(root.right, index + 1)
        
        if abs(left - right) > 1:
            return float("inf")
        return max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return False if self._isBalanced(root, 0) == float("inf") else True
