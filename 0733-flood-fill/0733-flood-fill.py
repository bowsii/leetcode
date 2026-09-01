class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(grid, i, j ,k, color, vis):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return
            if vis[i][j]==1:
                return 

            
             
            
            if grid[i][j]!=k:
                return
            grid[i][j]=color
            vis[i][j]=1
            dfs(grid,i,j-1,k,color,vis)
            dfs(grid,i,j+1,k,color,vis)
            dfs(grid,i-1,j,k,color,vis)
            dfs(grid,i+1,j,k,color,vis)
            
           
        vis=[[0]*len(grid[0]) for _ in range(len(grid))]
        strtcolor = grid[sr][sc]
        dfs(grid,sr,sc,strtcolor,color,vis)
        return grid

