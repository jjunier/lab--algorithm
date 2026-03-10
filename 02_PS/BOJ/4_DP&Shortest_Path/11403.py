import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

def find_reachability_matrix() -> None:
    node_count = int(input().strip())
    graph = [list(map(int, input().split())) for _ in range(node_count)]
    reachable = [[0] * node_count for _ in range(node_count)]

    for start_node in range(node_count):
        visited = [False] * node_count
        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()

            for next_node in range(node_count):
                if graph[current_node][next_node] == 1 and not visited[next_node]:
                    visited[next_node] = True
                    reachable[start_node][next_node] = 1
                    queue.append(next_node)

    output_lines = []

    for row in reachable:
        output_lines.append(" ".join(map(str, row)))

    output("\n".join(output_lines))

find_reachability_matrix()
