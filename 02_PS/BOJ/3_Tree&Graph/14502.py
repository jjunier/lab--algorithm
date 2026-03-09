import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
output = sys.stdout.write

def max_safe_area() -> None:
    row_count, col_count = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(row_count)]

    empty_cells = []
    virus_cells = []

    for row in range(row_count):
        for col in range(col_count):
            if lab[row][col] == 0:
                empty_cells.append((row, col))
            elif lab[row][col] == 2:
                virus_cells.append((row, col))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_safe_count = 0

    for walls in combinations(empty_cells, 3):
        # 연구소 복사
        copied_lab = [row[:] for row in lab]

        # 벽 3개 설치
        for wall_row, wall_col in walls:
            copied_lab[wall_row][wall_col] = 1

        # 바이러스 확산
        queue = deque(virus_cells)
        while queue:
            current_row, current_col = queue.popleft()

            for dr, dc in directions:
                next_row = current_row + dr
                next_col = current_col + dc

                if not (0 <= next_row < row_count and 0 <= next_col < col_count):
                    continue
                if copied_lab[next_row][next_col] != 0:
                    continue

                copied_lab[next_row][next_col] = 2
                queue.append((next_row, next_col))

        # 안전 영역 개수 세기
        safe_count = 0
        for row in range(row_count):
            for col in range(col_count):
                if copied_lab[row][col] == 0:
                    safe_count += 1

        max_safe_count = max(max_safe_count, safe_count)

    output(str(max_safe_count))

max_safe_area()