class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [1]*n
        for _ in range(m-1):
            c=[1]*n
            for i in range(1,n):
                c[i]=c[i-1]+a[i]
            a=c
            
        return a[-1]