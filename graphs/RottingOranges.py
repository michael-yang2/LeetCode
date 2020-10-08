class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        max_time = 0
        adj = [[-1,0],[1,0],[0,1],[0,-1]]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j,0))
        while rotten:
            row, col, time = rotten.popleft()
            if visited[row][col] or grid[row][col]==0:
                continue
            visited[row][col] = True
            max_time = max(max_time, time)
            for r,c in adj:
                if 0<= row+r < len(grid) and 0<=col+c < len(grid[0]) and not visited[row+r][col+c]:
                    rotten.append((row+r, col+c,time+1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    return -1
        return max_time