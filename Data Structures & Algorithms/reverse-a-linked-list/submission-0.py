# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# A B C D 
# a > b b > c c > d

# D C B A -> None
# d > c c > b b > a a > None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        previous_node = None

        while node:
            node_next = node.next
            node.next = previous_node
            previous_node = node

            if not node_next:
                break
            node = node_next
                      
        return node