# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val:
                if self.trees_comparison(node, subRoot):
                    return True

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False

    @staticmethod
    def trees_comparison(node1, node2):
        sub_stack = [(node1, node2)]
        while sub_stack:
            i, j = sub_stack.pop()

            if not i and not j:
                continue

            if not i or not j or i.val != j.val:
                return False
            
            sub_stack.extend(
                [(i.left, j.left), (i.right, j.right)]
            )
        
        return True