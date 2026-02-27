import sys
import heapq

input = sys.stdin.readline
output = sys.stdout.write

def min_bus_cost() -> None:
    city_count = int(input().strip())
    bus_count = int(input().strip())

    graph = [[] for _ in range(city_count + 1)]
    for _ in range(bus_count):
        from_city, to_city, cost = map(int, input().split())
        graph[from_city].append((to_city, cost))

    start_city, target_city = map(int, input().split())

    INF = 10**18
    min_cost = [INF] * (city_count + 1)
    min_cost[start_city] = 0

    heap = [(0, start_city)]  # (누적 비용, 도시)

    while heap:
        current_cost, current_city = heapq.heappop(heap)

        # 더 비싼 경로로 꺼낸 경우(낡은 정보) 무시
        if current_cost > min_cost[current_city]:
            continue

        # 목표 도시에 대한 최단 비용이 확정된 순간이므로 종료 가능
        if current_city == target_city:
            output(str(current_cost))
            return

        for next_city, edge_cost in graph[current_city]:
            new_cost = current_cost + edge_cost
            if new_cost < min_cost[next_city]:
                min_cost[next_city] = new_cost
                heapq.heappush(heap, (new_cost, next_city))

min_bus_cost()