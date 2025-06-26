class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surfarea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0 :
                    surfarea += 2
                if r == 0:
                    surfarea += grid[r][c]
                if c == 0:
                    surfarea += grid[r][c]
                if r == len(grid)-1:
                    surfarea += grid[r][c]
                if c == len(grid[0]) -1:
                    surfarea += grid[r][c]
                if r > 0 and grid[r-1][c] < grid[r][c]:
                    surfarea += grid[r][c] - grid[r-1][c]
                if r < len(grid[0])-1 and grid[r+1][c] < grid[r][c]:
                    surfarea += grid[r][c] - grid[r+1][c]
                if c > 0 and grid[r][c-1] < grid[r][c]:
                    surfarea += grid[r][c] - grid[r][c-1]
                if c < len(grid)-1 and grid[r][c+1] < grid[r][c]:
                    surfarea += grid[r][c] - grid[r][c+1]
        return surfarea
                    
                    
                    
        
        
        
