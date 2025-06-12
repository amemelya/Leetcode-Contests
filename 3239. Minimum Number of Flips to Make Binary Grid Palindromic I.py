class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows = 0
        cols = 0
        for r in range(len(grid)):
            cs = 0
            ce = len(grid[0]) -1
            while cs < ce:
                if grid[r][cs] != grid[r][ce]:
                    rows += 1
                cs += 1
                ce -= 1
        for c in range(len(grid[0])):
            rs = 0
            re = len(grid) - 1
            while rs < re:
                if grid[rs][c] != grid[re][c]:
                    cols += 1
                rs += 1
                re -= 1
        return min(rows,cols)
            
    
                
                
        
