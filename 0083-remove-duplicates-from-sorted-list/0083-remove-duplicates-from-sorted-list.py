# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        t = head
        if t is None:
            return head
        c = head.next
        while c!=None:
            if c.val == t.val:
                c = c.next
                t.next = c
            else:
                c=c.next
                t=t.next
        return head