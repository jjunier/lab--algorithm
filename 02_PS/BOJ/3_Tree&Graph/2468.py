import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def max_safe_areas() -> None:
    size = int(input().strip())
    height_map = [list(map(int, input().split())) for _ in range(size)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_height = min(min(row) for row in height_map)
    max_height = max(max(row) for row in height_map)

    def count_safe_areas(rain_height: int) -> int:
        visited = [[False] * size for _ in range(size)]
        area_count = 0

        for row in range(size):
            for col in range(size):
                # 아직 방문하지 않았고, 물에 잠기지 않은 칸이면 새로운 안전 영역 시작
                if not visited[row][col] and height_map[row][col] > rain_height:
                    area_count += 1
                    queue = deque([(row, col)])
                    visited[row][col] = True

                    while queue:
                        current_row, current_col = queue.popleft()

                        for dr, dc in directions:
                            next_row = current_row + dr
                            next_col = current_col + dc

                            if not (0 <= next_row < size and 0 <= next_col < size):
                                continue
                            if visited[next_row][next_col]:
                                continue
                            if height_map[next_row][next_col] <= rain_height:
                                continue

                            visited[next_row][next_col] = True
                            queue.append((next_row, next_col))

        return area_count

    # 비가 전혀 오지 않는 경우(0)도 포함해야 함
    max_area_count = 0
    for rain_height in range(0, max_height + 1):
        max_area_count = max(max_area_count, count_safe_areas(rain_height))

    output(str(max_area_count))

max_safe_areas()