import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def count_connected_components() -> None:
    node_count, edge_count = map(int, input().split())
    graph = [[] for _ in range(node_count + 1)]

    for _ in range(edge_count):
        node_a, node_b = map(int, input().split())
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    visited = [False] * (node_count + 1)
    component_count = 0

    for start_node in range(1, node_count + 1):
        if visited[start_node]:
            continue

        # 새로운 연결 요소 발견
        component_count += 1
        queue = deque([start_node])
        visited[start_node] = True

        while queue:
            current_node = queue.popleft()

            for next_node in graph[current_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

    output(str(component_count))

count_connected_components()