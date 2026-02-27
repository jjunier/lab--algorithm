import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def min_days_to_ripen_tomatoes_3d() -> None:
    col_count, row_count, height_count = map(int, input().split())  # M, N, H

    # box[z][r][c]  (z: 층, r: 행, c: 열)
    box = []
    queue = deque()
    unripe_count = 0

    for z in range(height_count):
        layer = []
        for r in range(row_count):
            row = list(map(int, input().split()))
            layer.append(row)

            for c in range(col_count):
                if row[c] == 1:
                    queue.append((z, r, c))  # 익은 토마토는 시작점
                elif row[c] == 0:
                    unripe_count += 1        # 익지 않은 토마토 개수 카운트
        box.append(layer)

    # 처음부터 모두 익어있으면 0
    if unripe_count == 0:
        print(0)
        return

    # 6방향: 위/아래(층 이동), 앞/뒤/좌/우(2D 이동)
    directions = [
        (0, -1, 0), (0, 1, 0),   # 행 이동
        (0, 0, -1), (0, 0, 1),   # 열 이동
        (-1, 0, 0), (1, 0, 0)    # 층 이동
    ]

    days = -1  # 레벨(하루) 단위 BFS

    while queue:
        days += 1
        for _ in range(len(queue)):
            current_z, current_r, current_c = queue.popleft()

            for dz, dr, dc in directions:
                next_z = current_z + dz
                next_r = current_r + dr
                next_c = current_c + dc

                if not (0 <= next_z < height_count and 0 <= next_r < row_count and 0 <= next_c < col_count):
                    continue

                # 익지 않은 토마토(0)만 익힐 수 있음
                if box[next_z][next_r][next_c] == 0:
                    box[next_z][next_r][next_c] = 1
                    unripe_count -= 1
                    queue.append((next_z, next_r, next_c))

    output(str(days if unripe_count == 0 else -1))

min_days_to_ripen_tomatoes_3d()