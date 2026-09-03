class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c:
                return 0
            if grid[i][j]!=1:
                return 0
            grid[i][j]=0
            area = 1
            area += dfs(i-1,j)
            area += dfs(i+1,j)
            area += dfs(i,j-1)
            area += dfs(i,j+1)
            return area
        r = len(grid)
        c = len(grid[0])
        mx = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                   
                    a=dfs(i,j)
                    mx = max(mx,a)
        return mx