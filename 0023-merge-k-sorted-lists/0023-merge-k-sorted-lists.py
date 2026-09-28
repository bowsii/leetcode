# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, l: list[ListNode | None]) -> ListNode | None:
        if not l or len(l)==0:
            return None
        def ml(l1,l2):
            node = ListNode()
            ans = node
            while l1 and l2:
                if l1.val > l2.val:
                    node.next = l2
                    l2 = l2.next
                else:
                    node.next = l1
                    l1 = l1.next
                node = node.next
            if l1:
                node.next = l1
            else:
                node.next = l2
            return ans.next
        while len(l) > 1:
            t = []
            for i in range(0,len(l),2):
                l1 = l[i]
                l2 = l[i+1] if i+1 < len(l) else None
                t.append(ml(l1,l2))
            l=t
        return l[0]
    