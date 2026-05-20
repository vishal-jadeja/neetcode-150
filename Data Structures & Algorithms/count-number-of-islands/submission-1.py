class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr in range(ROWS) and
                       nc in range(COLS) and
                       grid[nr][nc] == "1" and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands