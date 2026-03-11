import sys

input = sys.stdin.readline
output = sys.stdout.write

def all_pairs_shortest_path() -> None:
    city_count = int(input().strip())
    bus_count = int(input().strip())
    INF = 10**15
    min_cost = [[INF] * (city_count + 1) for _ in range(city_count + 1)]
    
    # 자기 자신으로 가는 비용은 0
    for city in range(1, city_count + 1):
        min_cost[city][city] = 0
        
    # 같은 출발-도착 쌍의 버스가 여러 개 있을 수 있으므로 최소값만 저장
    for _ in range(bus_count):
        start_city, end_city, cost = map(int, input().split())
        if cost < min_cost[start_city][end_city]:
            min_cost[start_city][end_city] = cost
            
    # Floyd-Warshall
    for mid_city in range(1, city_count + 1):
        for start_city in range(1, city_count + 1):
            for end_city in range(1, city_count + 1):
                if min_cost[start_city][end_city] > min_cost[start_city][mid_city] + min_cost[mid_city][end_city]:
                    min_cost[start_city][end_city] = min_cost[start_city][mid_city] + min_cost[mid_city][end_city]
                    
    output_lines = []
    
    for start_city in range(1, city_count + 1):
        row = []
        
        for end_city in range(1, city_count + 1):
            if min_cost[start_city][end_city] == INF:
                row.append("0")
                
            else:
                row.append(str(min_cost[start_city][end_city]))
        
        output_lines.append(" ".join(row))
                
    output("\n".join(output_lines))
        
all_pairs_shortest_path()