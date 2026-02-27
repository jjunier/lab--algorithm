import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def min_days_ripe_tomatoes() -> None:
    col_count, row_count = map(int, input().split())    # M, N
    box = [list(map(int, input().split())) for _ in range(row_count)]

    queue = deque()
    unripe_count = 0

    # 시작 시점의 익은 토마토(1)는 전부 큐에 넣고,
    # 익지 않은 토마토(0)는 개수를 세어둔다.
    for row in range(row_count):
        for col in range(col_count):
            if box[row][col] == 1:
                queue.append((row, col))
            elif box[row][col] == 0:
                unripe_count += 1

    # 처음부터 전부 익어있다면
    if unripe_count == 0:
        print(0)
        return

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    days = -1  # 레벨(하루) 단위 BFS를 위해 -1에서 시작
    
    # BFS: 하루 단위(레벨 단위)로 진행
    while queue:
        days += 1
        for _ in range(len(queue)):
            current_row, current_col = queue.popleft()
            
            for dr, dc in directions:
                next_row = current_row + dr
                next_col = current_col + dc
                
                if not(0 <= next_row < row_count and 0 <= next_col < col_count):
                    continue
                    
                # 익지 않은 토마토(0)만 익히기
                if box[next_row][next_col] == 0:
                    box[next_row][next_col] = 1
                    unripe_count -= 1
                    queue.append((next_row, next_col))
                    
    # BFS 알고리즘 후 안 익은 토마토 존재 시 불가능(-1) 반환
    output(str(days if unripe_count == 0 else -1))
    
min_days_ripe_tomatoes()