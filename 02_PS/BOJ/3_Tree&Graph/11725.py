import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def find_parents_tree() -> None:
    node_count = int(input())
    graph = [[] for _ in range(node_count + 1)]
    
    # 무방향 간선 입력
    for _ in range(node_count - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    parent = [0] * (node_count + 1)    # parent[i]: i의 부모 노드
    queue = deque([1])
    parent[1] = -1
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            # 아직 부모노드가 정해지지 않은 노드 = 방문하지 않은 노드
            if parent[neighbor] == 0:
                parent[neighbor] = current
                queue.append(neighbor)
                
    # 2번부터 N번까지의 부모노드 출력
    output("\n".join(str(parent[i]) for i in range(2, node_count + 1)))
        
find_parents_tree()