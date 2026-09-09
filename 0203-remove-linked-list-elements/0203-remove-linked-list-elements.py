# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans  = ListNode(0,head)
        d = ans

        while d:
            while d.next and d.next.val==val:
                d.next = d.next.next
            d = d.next
        return ans.next