# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        t = head
        s=''
        while t is not None:
            s += str(t.val)
            t = t.next
        v = int(s,2)
        return v