from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([(0, 0, 1)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    
    return -1