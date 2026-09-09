# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        arr = []

        curr = head

        while curr:
            if curr.val != val:
                arr.append(curr.val)

            curr = curr.next

        new_head = ListNode()
        new_curr = new_head
        for n in arr:
            new_curr.next = ListNode(n)
            new_curr = new_curr.next

        return new_head.next
