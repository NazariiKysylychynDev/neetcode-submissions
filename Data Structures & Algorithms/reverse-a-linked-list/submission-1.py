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
        prev, cur = None, head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
                      
        return prev