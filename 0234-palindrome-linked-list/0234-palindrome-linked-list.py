# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        r = []
        c = head
        while c:
            r.append(c.val)
            c = c.next
        return r == r[::-1]