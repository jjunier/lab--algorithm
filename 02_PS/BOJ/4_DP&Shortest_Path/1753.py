import sys
import heapq

input = sys.stdin.readline
output = sys.stdout.write

def shortest_paths_dijkstra() -> None:
    vertex_count, edge_count = map(int, input().split())
    start_vertex = int(input().strip())

    # 인접 리스트 그래프 구성
    # graph[u] = [(v, w), ...] -> u에서 v로 가는 가중치 w
    graph = [[] for _ in range(vertex_count + 1)]
    for _ in range(edge_count):
        from_vertex, to_vertex, weight = map(int, input().split())
        graph[from_vertex].append((to_vertex, weight))

    INF = 10**18
    distance = [INF] * (vertex_count + 1)    # 시작 정점: 현재까지 알려진 최단 거리
    distance[start_vertex] = 0

    # 최소 힙 (우선 순위 큐 사용)
    heap = [(0, start_vertex)]  # (현재까지의 거리, 정점 번호)

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        # 더 짧은 경로로 이미 방문(확정)된 상태면 스킵
        if current_dist > distance[current_vertex]:
            continue
        # 현재 정점에서 갈 수 있는 모든 인접 정점 확인
        for next_vertex, weight in graph[current_vertex]:
            new_dist = current_dist + weight
            
            # 더 짧은 경로 발견 시 갱신하기
            if new_dist < distance[next_vertex]:
                distance[next_vertex] = new_dist
                heapq.heappush(heap, (new_dist, next_vertex))

    out_lines = []
    for vertex in range(1, vertex_count + 1):
        if distance[vertex] == INF:
            out_lines.append("INF")    # 도달 불가능 종결
        else:
            out_lines.append(str(distance[vertex]))

    output(str("\n".join(out_lines)))

shortest_paths_dijkstra()