# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([root])
        r=[]
        while q:
            l=len(q)
            cl=[]
            for i in range(l):
                n = q.popleft()
                cl.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            r.append(cl)
        re=[]
        for i in range(len(r)-1,-1,-1):
            a=[]
            for j in range(len(r[i])):
                a.append(r[i][j])
            re.append(a)
        return re
        