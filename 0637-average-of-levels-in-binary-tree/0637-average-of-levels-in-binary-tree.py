# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue=deque([root])
        r=[]
        while queue:
            l=len(queue)
            cl=[]
            for i in range(l):
                node = queue.popleft()
                cl.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            r.append(cl)
        re=[]
        for i in r:
            re.append((sum(i)/len(i)))
        return re