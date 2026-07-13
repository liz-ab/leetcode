class Solution(object):
    def numIslands(self, grid):
        if not grid: 
            return 0
        row=len(grid)
        col=len(grid[0])
        
        def dfs(r,c):
            if r<0 or c<0 or r>row-1 or c>col-1 or grid[r][c]=='0':
                return 
            grid[r][c]='0'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        co = 0
        for i in range(0,row):
          for j in range(0,col):
                if(grid[i][j]=='1'):
                 dfs(i,j)
                 co+=1
        return co
        