import sys
import heapq

input = sys.stdin.readline

def dijkstra(start_node: int, graph: list[list[tuple[int, int]]], node_count: int) -> list[int]:
    INF = 10**18
    distance = [INF] * (node_count + 1)
    distance[start_node] = 0

    heap = [(0, start_node)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > distance[current_node]:
            continue

        for next_node, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return distance


def shortest_special_path() -> None:
    node_count, edge_count = map(int, input().split())

    graph = [[] for _ in range(node_count + 1)]
    for _ in range(edge_count):
        node_a, node_b, weight = map(int, input().split())
        graph[node_a].append((node_b, weight))
        graph[node_b].append((node_a, weight))

    must_visit_1, must_visit_2 = map(int, input().split())

    dist_from_1 = dijkstra(1, graph, node_count)
    dist_from_v1 = dijkstra(must_visit_1, graph, node_count)
    dist_from_v2 = dijkstra(must_visit_2, graph, node_count)

    INF = 10**18

    # 경로 1: 1 -> v1 -> v2 -> N
    path_1 = dist_from_1[must_visit_1] + dist_from_v1[must_visit_2] + dist_from_v2[node_count]

    # 경로 2: 1 -> v2 -> v1 -> N
    path_2 = dist_from_1[must_visit_2] + dist_from_v2[must_visit_1] + dist_from_v1[node_count]

    answer = min(path_1, path_2)

    print(answer if answer < INF else -1)

shortest_special_path()