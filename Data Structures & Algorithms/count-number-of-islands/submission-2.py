class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])

        island = 0

        def dfs(row, col):
            # boundry check - recursion breaking condition
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            # if we found water - 0
            if grid[row][col] == "0":
                return
            # mark the visited land as water for avoding visiting it again
            grid[row][col] = "0"

            # eplore all four direction of it
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row,col+1)
            dfs(row,col-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island += 1
                    dfs(row, col)
            
        return island