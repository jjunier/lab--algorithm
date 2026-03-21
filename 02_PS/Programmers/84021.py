from collections import deque

def solution(game_board, table):
    n = len(game_board)

    def bfs(board, target):
        visited = [[False] * n for _ in range(n)]
        shapes = []

        for i in range(n):
            for j in range(n):
                if board[i][j] == target and not visited[i][j]:
                    queue = deque([(i, j)])
                    visited[i][j] = True
                    cells = [(0, 0)]
                    origin_x, origin_y = i, j

                    while queue:
                        x, y = queue.popleft()

                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy

                            if 0 <= nx < n and 0 <= ny < n:
                                if board[nx][ny] == target and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
                                    cells.append((nx - origin_x, ny - origin_y))

                    shapes.append(normalize(cells))

        return shapes

    def normalize(shape):
        min_x = min(x for x, y in shape)
        min_y = min(y for x, y in shape)
        normalized = sorted((x - min_x, y - min_y) for x, y in shape)
        return tuple(normalized)

    def rotate(shape):
        rotated = [(-y, x) for x, y in shape]
        return normalize(rotated)

    blanks = bfs(game_board, 0)
    pieces = bfs(table, 1)

    used = [False] * len(pieces)
    answer = 0

    for blank in blanks:
        for i in range(len(pieces)):
            if used[i] or len(blank) != len(pieces[i]):
                continue

            piece = pieces[i]
            matched = False

            for _ in range(4):
                if blank == piece:
                    matched = True
                    break
                piece = rotate(piece)

            if matched:
                used[i] = True
                answer += len(blank)
                break

    return answer