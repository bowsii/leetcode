# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=ListNode()
        
        prev = None
        c = head
        while (c!=None):
            next = c.next
            c.next = prev
            prev = c
            c = next
        head = prev
        return head
