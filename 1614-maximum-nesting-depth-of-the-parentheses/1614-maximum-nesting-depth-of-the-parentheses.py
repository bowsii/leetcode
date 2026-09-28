class Solution:
    def maxDepth(self, s: str) -> int:
        d = 0
        md = 0
        for i in s:
            if i==')':
                d-=1
            if i=='(':
                d+=1
            md = max(d,md)
        return md