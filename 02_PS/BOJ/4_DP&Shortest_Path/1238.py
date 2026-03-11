import sys
import heapq

input = sys.stdin.readline
output = sys.stdout.write

def max_round_trip_time() -> None:
    village_count, road_count, party_village = map(int, input().split())

    graph = [[] for _ in range(village_count + 1)]
    reverse_graph = [[] for _ in range(village_count + 1)]

    for _ in range(road_count):
        start, end, time_cost = map(int, input().split())
        graph[start].append((end, time_cost))
        reverse_graph[end].append((start, time_cost))

    def dijkstra(start_node: int, graph_data: list[list[tuple[int, int]]]) -> list[int]:
        INF = 10**15
        distance = [INF] * (village_count + 1)
        distance[start_node] = 0

        heap = [(0, start_node)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)

            if current_dist > distance[current_node]:
                continue

            for next_node, edge_cost in graph_data[current_node]:
                new_dist = current_dist + edge_cost
                if new_dist < distance[next_node]:
                    distance[next_node] = new_dist
                    heapq.heappush(heap, (new_dist, next_node))

        return distance

    # party_village -> 각 마을
    go_home_distance = dijkstra(party_village, graph)

    # 각 마을 -> party_village
    # 간선을 뒤집은 그래프에서 party_village부터 최단거리 구하면 됨
    go_party_distance = dijkstra(party_village, reverse_graph)

    max_time = 0
    for village in range(1, village_count + 1):
        round_trip_time = go_party_distance[village] + go_home_distance[village]
        max_time = max(max_time, round_trip_time)

    output(str(max_time))

max_round_trip_time()