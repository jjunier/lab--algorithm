import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def dfs_bfs_traversal() -> None:
    node_count, edge_count, start_node = map(int, input().split())
    graph = [[] for _ in range(node_count + 1)]
    
    for _ in range(edge_count):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    # 정점 번호가 작은 것부터 방문해야 하므로 정렬을 선 진행
    for node in range(1, node_count + 1):
        graph[node].sort()
        
    # DFS 구현 (stack)
    def dfs(start: int) -> list[int]:
        visited = [False] * (node_count + 1)
        order: list[int] = []    
        stack = [start]
        
        while stack:
            current = stack.pop()
            if visited[current]:
                continue
                
            visited[current] = True
            order.append(current)
            
            for neighbor in reversed(graph[current]):
                if not visited[neighbor]:
                    stack.append(neighbor)
                    
        return order
    
    # BFS 구현 (queue)
    def bfs(start: int) -> list[int]:
        visited = [False] * (node_count + 1)
        order: list[int] = []
        queue = deque([start])
        visited[start] = True
        
        while queue:
            current = queue.popleft()
            order.append(current)
            
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    
        return order
    
    dfs_order = dfs(start_node)
    bfs_order = bfs(start_node)
    
    output(" ".join(map(str, dfs_order)) + "\n")
    output(" ".join(map(str, bfs_order)))
    
dfs_bfs_traversal()