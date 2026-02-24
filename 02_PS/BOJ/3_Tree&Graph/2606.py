import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def count_infected_computers() -> None:
    computer_count = int(input().strip())
    connection_count = int(input().strip())
    graph = [[] for _ in range(computer_count + 1)]
    
    for _ in range(connection_count):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False] * (computer_count + 1)
    visited[1] = True
    
    queue = deque([1])
    infected_count = 0    # 1번 제외, 새로 감염된 컴퓨터의 수
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                infected_count += 1
                queue.append(neighbor)
            
    print(infected_count)
    
count_infected_computers()