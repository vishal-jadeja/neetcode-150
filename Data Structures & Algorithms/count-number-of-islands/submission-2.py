class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr in range(ROWS) and
                    nc in range(COLS) and
                    grid[nr][nc] == "1" and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    dfs(nr, nc)
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1
        return islands