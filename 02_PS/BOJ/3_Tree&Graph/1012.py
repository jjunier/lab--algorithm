import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def count_worms_for_all_tests() -> None:
    test_case_count = int(input().strip())
    
    # 상, 하, 좌, 우 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count_worms: list[str] = []
        
    for _ in range(test_case_count):
        width, height, cabbage_count = map(int, input().split())

        # 배추밭 초기화 (0: 없음, 1: 배추 있음)
        field = [[0] * width for _ in range(height)]

        # 배추 위치 표시
        for _ in range(cabbage_count):
            x, y = map(int, input().split())
            field[y][x] = 1 # y: 행, x: 열
            
        visited = [[False] * width for _ in range(height)]
        worm_count = 0    # 필요한 지렁이의 수 ( = 연결 요소의 개수)
        
        for row in range(height):
            for col in range(width):
                # 아직 방문하지 않은 배추 발견 -> 새로운 단지의 시작
                if field[row][col] == 1 and not visited[row][col]:
                    worm_count += 1
                    queue = deque([(row,col)])
                    visited[row][col] = True
                    
                    # BFS로 인접한 배추를 모두 탐색
                    while queue:
                        current_row, current_col = queue.popleft()
                        
                        for dr, dc in directions:
                            next_row = current_row + dr
                            next_col = current_col + dc
                            
                            # 범위 체크
                            if not (0 <= next_row < height and 0 <= next_col < width):
                                continue
                            # 이미 방문했거나 배추가 아니면 스킵
                            if visited[next_row][next_col] or field[next_row][next_col] == 0:
                                continue
                                
                            visited[next_row][next_col] = True
                            queue.append((next_row, next_col))
                            
        count_worms.append(str(worm_count))
        
    output("\n".join(count_worms))
                
count_worms_for_all_tests()