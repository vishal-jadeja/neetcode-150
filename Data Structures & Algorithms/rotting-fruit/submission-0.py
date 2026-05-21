class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh, time = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr, nc])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1