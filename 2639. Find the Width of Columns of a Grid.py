class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        res = []
        for col in range(cols):
            wid = 0
            for row in range(rows):
                w = len(str(grid[row][col]))
                #print(w)
                wid = max(w,wid)
            res.append(wid)
        return res
                
                
        
