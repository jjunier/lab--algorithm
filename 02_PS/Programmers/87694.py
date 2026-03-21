from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]

    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    board[x][y] = 2
                elif board[x][y] != 2:
                    board[x][y] = 1

    queue = deque([(characterX * 2, characterY * 2, 0)])
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, dist = queue.popleft()

        if x == itemX * 2 and y == itemY * 2:
            return dist // 2

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 102 and 0 <= ny < 102:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))