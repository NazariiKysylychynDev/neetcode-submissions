# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0

        left = 1 + self._isBalanced(root.left)
        right = 1 + self._isBalanced(root.right)
        
        if not -1 >= left - right <= 1:
            return float("-inf")
        return max(left, right)
    
    def isBalanced(self, root):
        res = self._isBalanced(root)
        return False if res == float("-inf") else True
