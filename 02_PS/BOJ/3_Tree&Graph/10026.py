import sys
from collections import deque

input = sys.stdin.readline

def count_color_regions() -> None:
    size = int(input().strip())
    grid = [list(input().strip()) for _ in range(size)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start_row: int, start_col: int, visited: list[list[bool]], color_blind: bool) -> None:
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        start_color = grid[start_row][start_col]

        while queue:
            current_row, current_col = queue.popleft()

            for dr, dc in directions:
                next_row = current_row + dr
                next_col = current_col + dc

                if not (0 <= next_row < size and 0 <= next_col < size):
                    continue
                if visited[next_row][next_col]:
                    continue

                next_color = grid[next_row][next_col]

                if color_blind:
                    # 적록색약은 R과 G를 같은 색으로 봄
                    if start_color in ('R', 'G'):
                        if next_color not in ('R', 'G'):
                            continue
                    else:
                        if next_color != start_color:
                            continue
                else:
                    if next_color != start_color:
                        continue

                visited[next_row][next_col] = True
                queue.append((next_row, next_col))

    def count_regions(color_blind: bool) -> int:
        visited = [[False] * size for _ in range(size)]
        region_count = 0

        for row in range(size):
            for col in range(size):
                if not visited[row][col]:
                    bfs(row, col, visited, color_blind)
                    region_count += 1

        return region_count

    normal_count = count_regions(False)
    color_blind_count = count_regions(True)

    print(normal_count, color_blind_count)

count_color_regions()