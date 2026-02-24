import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def count_complexes() -> None:
    size = int(input().strip())
    grid = [list(map(int, input().strip())) for _ in range(size)]
    
    visited = [[False] * size for _ in range(size)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    complex_sizes: list[int] = []
        
    for row in range(size):
        for col in range(size):
            if grid[row][col] == 1 and not visited[row][col]:
                queue = deque([(row, col)])
                visited[row][col] = True
                house_count = 1
                
                while queue:
                    current_row, current_col = queue.popleft()
                    
                    for dr, dc in directions:
                        next_row = current_row + dr
                        next_col = current_col + dc
                        
                        if not (0 <= next_row < size and 0 <= next_col < size):
                            continue
                        if visited[next_row][next_col]:
                            continue
                        if grid[next_row][next_col] == 0:
                            continue
                            
                        visited[next_row][next_col] = True
                        house_count += 1
                        queue.append((next_row, next_col))
                        
                complex_sizes.append(house_count)
                
    complex_sizes.sort()
    
    output(str(len(complex_sizes)) + "\n")
    output("\n".join(map(str, complex_sizes)))

count_complexes()