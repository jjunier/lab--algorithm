import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def min_time_to_find_sibling() -> None:
    start_position, target_position = map(int, input().split())

    # 이미 앞에 있거나 같은 위치라면 뒤로 가기
    if start_position >= target_position:
        output(str(start_position - target_position))
        return 
    
    max_position = 100_000
    visited = [-1] * (max_position + 1)
    visited[start_position] = 0
    queue = deque([start_position])

    while queue:
        current_position = queue.popleft()

        if current_position == target_position:
            output(str(visited[current_position]))
            return
        
        for next_position in (
            current_position - 1,
            current_position + 1,
            current_position * 2,
        ):
            if 0 <= next_position <= max_position and visited[next_position] == -1:
                visited[next_position] = visited[current_position] + 1
                queue.append(next_position)

min_time_to_find_sibling()