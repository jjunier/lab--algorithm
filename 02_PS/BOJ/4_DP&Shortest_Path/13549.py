import sys
from collections import deque

input = sys.stdin.readline

def min_time_to_find_sibling() -> None:
    start_position, target_position = map(int, input().split())

    max_position = 100000
    INF = 10**9

    distance = [INF] * (max_position + 1)
    distance[start_position] = 0

    queue = deque([start_position])

    while queue:
        current_position = queue.popleft()

        if current_position == target_position:
            print(distance[current_position])
            return

        # 순간이동: 0초
        next_position = current_position * 2
        if 0 <= next_position <= max_position and distance[next_position] > distance[current_position]:
            distance[next_position] = distance[current_position]
            queue.appendleft(next_position)

        # 걷기: 1초
        next_position = current_position - 1
        if 0 <= next_position <= max_position and distance[next_position] > distance[current_position] + 1:
            distance[next_position] = distance[current_position] + 1
            queue.append(next_position)

        next_position = current_position + 1
        if 0 <= next_position <= max_position and distance[next_position] > distance[current_position] + 1:
            distance[next_position] = distance[current_position] + 1
            queue.append(next_position)

min_time_to_find_sibling()