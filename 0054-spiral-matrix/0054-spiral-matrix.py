class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        t=0
        l=0
        b=len(m)-1
        r=len(m[0])-1
        s=[]
        while t<=b and l<=r:
            for i in range(l,r+1):
                s.append(m[t][i])
            t+=1
            for j in range(t,b+1):
                s.append(m[j][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    s.append(m[b][i])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    s.append(m[i][l])
                l+=1
        return s