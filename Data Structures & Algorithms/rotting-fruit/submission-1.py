class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        queue = deque()

        # find all the rotten oragens in the grid first
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1
        # creating a direction set to find all the adjecent fruits in all direction
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        mins = 0
        while queue and fresh > 0:
            level_size = len(queue)

            for i in range(level_size):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and 
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))

            mins += 1
        
        if fresh == 0:
            return mins
        else:
            return -1