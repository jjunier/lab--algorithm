import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def tree_diameter() -> None:
    node_count = int(input().strip())
    graph = [[] for _ in range(node_count + 1)]

    for _ in range(node_count - 1):
        parent_node, child_node, weight = map(int, input().split())
        
        graph[parent_node].append((child_node, weight))
        graph[child_node].append((parent_node, weight))

    def farthest_from(start_node: int) -> tuple[int, int]:
        distance = [-1] * (node_count + 1)
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
            
        for node in range(1, node_count + 1):
            if distance[node] > farthest_dist:
                farthest_dist = distance[node]
                farthest_node = node
                    
        return farthest_node, farthest_dist
        
    # 1. 임의의 점(1)에서 가장 먼 점 A
    node_a, _ = farthest_from(1)
    # 2. A에서 가장 먼점까지의 거리 (지름)
    _, diameter = farthest_from(node_a)
        
    output(str(diameter))

tree_diameter()