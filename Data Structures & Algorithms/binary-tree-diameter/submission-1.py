# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _diameterOfBinaryTree(self, root: TreeNode) -> (int, int):
        if not root:
            return 0, 0
        

        left, left_score = self._diameterOfBinaryTree(root.left)
        right, right_score = self._diameterOfBinaryTree(root.right)

        return 1 + max(left, right), max(left + right, left_score, right_score)

        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self._diameterOfBinaryTree(root)[1]