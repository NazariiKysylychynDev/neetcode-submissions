# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue = deque([(p, q)])

        while queue:
            i, j = queue.popleft()

            if i is None and j is None:
                continue

            if type(i) != type(j) or i.val != j.val:
                break

            queue.append((i.left, j.left))
            queue.append((i.right, j.right))
        else:
            return True
        return False 
