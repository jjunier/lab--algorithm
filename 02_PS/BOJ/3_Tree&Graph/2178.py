import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def shortest_path_maze() -> None:
    row_count, col_count = map(int, input().split())
    maze = [list(map(int, input().strip())) for _ in range(row_count)]
    
    # 거리 배열(0: 미방문), 시작점은 1칸으로 카운트
    distance = [[0] * col_count for _ in range(row_count)]
    distance[0][0] = 1
    
    queue = deque([(0, 0)])
    
    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        current_row, current_col = queue.popleft()
        
        for dr, dc in directions:
            next_row = current_row + dr
            next_col = current_col + dc
            
            # 범위 밖이면 무시
            if not(0 <= next_row < row_count and 0 <= next_col < col_count):
                continue
                
            # 벽이 0이면 이동 불가
            if maze[next_row][next_col] == 0:
                continue
                
            # 이미 방문하였다면 스킵
            if distance[next_row][next_col] != 0:
                continue
                
            distance[next_row][next_col] = distance[current_row][current_col] + 1
            queue.append((next_row, next_col))
            
    output(str(distance[row_count - 1][col_count - 1]))

shortest_path_maze()