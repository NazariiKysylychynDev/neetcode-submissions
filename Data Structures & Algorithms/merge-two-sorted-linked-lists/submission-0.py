# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# list1 = [1,2,4], list2 = [1,3,5], head [None]
# list1 = 1, list2 = 1, tail None
# list1 = 1, list2 = 3, tail 2.1 next_node=2.1
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = head = ListNode(None)

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = tail = list1
                list1 = list1.next      
            else:
                tail.next = tail = list2
                list2 = list2.next
        tail.next = list1 if list1 else list2
        return head.next