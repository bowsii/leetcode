# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        r=[]
        cur=head
        while cur:
            r.append(cur.val)
            cur=cur.next
        return r==r[::-1]