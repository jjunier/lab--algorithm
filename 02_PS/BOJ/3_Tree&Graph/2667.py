import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def count_complexes() -> None:
    size = int(input().strip())
    # 문자열로 붙어 입력되기 때문에 한 글자씩 int형으로 변환
    grid = [list(map(int, input().strip())) for _ in range(size)]
    
    # 방문 여부 체크를 위한 배열
    visited = [[False] * size for _ in range(size)]

    # 상, 하, 좌, 우 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    complex_sizes: list[int] = []
        
    for row in range(size):
        for col in range(size):
            # 집(1)이고 아직 방문하지 않았다면 새로운 단지 시작
            if grid[row][col] == 1 and not visited[row][col]:
                queue = deque([(row, col)])
                visited[row][col] = True
                house_count = 1 # 현재 단지의 집 수

                # BFS로 연결된 집들 탐색
                while queue:
                    current_row, current_col = queue.popleft()
                    
                    for dr, dc in directions:
                        next_row = current_row + dr
                        next_col = current_col + dc
                        
                        # 범위 체크
                        if not (0 <= next_row < size and 0 <= next_col < size):
                            continue
                        # 이미 방문했거나 집이 아니라면 스킵
                        if visited[next_row][next_col]:
                            continue
                        if grid[next_row][next_col] == 0:
                            continue
                            
                        visited[next_row][next_col] = True
                        house_count += 1
                        queue.append((next_row, next_col))
                
                # 하나의 단지 탐색 완료
                complex_sizes.append(house_count)
    
    # 단지별 집 수 오름차순 정렬
    complex_sizes.sort()
    
    # 결과 출력
    output(str(len(complex_sizes)) + "\n")
    output("\n".join(map(str, complex_sizes)))

count_complexes()