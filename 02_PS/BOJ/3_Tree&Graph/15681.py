import sys

input = sys.stdin.readline
output = sys.stdout.write

sys.setrecursionlimit(10**6)

def count_subtree_nodes() -> None:
    node_count, root_node, query_count = map(int, input().split())

    graph = [[] for _ in range(node_count + 1)]
    for _ in range(node_count - 1):
        node_a, node_b = map(int, input().split())
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    # subtree_size[u] = u를 루트로 하는 서브트리의 정점 수
    subtree_size = [0] * (node_count + 1)
    visited = [False] * (node_count + 1)

    def dfs(current_node: int) -> int:
        visited[current_node] = True
        subtree_size[current_node] = 1  # 자기 자신 포함

        for next_node in graph[current_node]:
            if not visited[next_node]:
                subtree_size[current_node] += dfs(next_node)

        return subtree_size[current_node]

    # 루트 기준으로 한 번만 DFS 수행
    dfs(root_node)

    output_lines = []
    for _ in range(query_count):
        query_node = int(input().strip())
        output_lines.append(str(subtree_size[query_node]))

    output("\n".join(output_lines))

count_subtree_nodes()