import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def min_knight_moves() -> None:
    test_case_count = int(input().strip())
    outputs: list[str] = []

    # 나이트의 8가지 이동
    knight_moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1),
    ]

    for _ in range(test_case_count):
        board_size = int(input().strip())
        start_row, start_col = map(int, input().split())
        target_row, target_col = map(int, input().split())

        # 시작 == 도착이면 0
        if start_row == target_row and start_col == target_col:
            outputs.append("0")
            continue

        distance = [[-1] * board_size for _ in range(board_size)]
        distance[start_row][start_col] = 0
        queue = deque([(start_row, start_col)])

        while queue:
            current_row, current_col = queue.popleft()

            for dr, dc in knight_moves:
                next_row = current_row + dr
                next_col = current_col + dc

                if not (0 <= next_row < board_size and 0 <= next_col < board_size):
                    continue
                if distance[next_row][next_col] != -1:
                    continue

                distance[next_row][next_col] = distance[current_row][current_col] + 1

                # 목표 지점에 도착하면 그 순간이 최단 거리
                if next_row == target_row and next_col == target_col:
                    outputs.append(str(distance[next_row][next_col]))
                    queue.clear()  # while 탈출용
                    break

                queue.append((next_row, next_col))

    output(str("\n".join(outputs)))

min_knight_moves()