import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def tree_diameter() -> None:
    vertex_count = int(input().strip())
    graph = [[] for _ in range(vertex_count + 1)]
    
    for _ in range(vertex_count):
        data = list(map(int, input().split()))
        node = data[0]
        idx = 1
        
        while data[idx] != -1:
            neighbor = data[idx]
            weight = data[idx + 1]
            graph[node].append((neighbor, weight))
            idx += 2
            
    def farthest_from(start_node: int) -> tuple[int, int]:
        distance = [-1] * (vertex_count + 1)
        distance[start_node] = 0
        queue = deque([start_node])
        
        while queue:
            current = queue.popleft()
            for neighbor, w in graph[current]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[current] + w
                    queue.append(neighbor)
                    
        farthest_node = start_node
        farthest_dist = 0
        
        for node in range(1, vertex_count + 1):
            if distance[node] > farthest_dist:
                farthest_dist = distance[node]
                farthest_node = node
                
        return farthest_node, farthest_dist
    
    node_a, _ = farthest_from(1)
    _, diameter = farthest_from(node_a)
    
    output(str(diameter))
    
tree_diameter()       