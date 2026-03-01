import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_travel_cost() -> None:
    city_count = int(input().strip())
    road_lengths = list(map(int, input().split()))
    fuel_prices = list(map(int, input().split()))
    min_price_so_far = fuel_prices[0]
    total_cost = 0
    
    for i in range(city_count - 1):
        # 만약 더 싼 주유소를 만난다면 갱신하기
        if fuel_prices[i] < min_price_so_far:
            min_price_so_far = fuel_prices[i]
        
        # 현재까지의 최소 가격으로 다음 도시까지 이동할 기름 구매하기
        total_cost += min_price_so_far * road_lengths[i]
        
    print(total_cost)
    
min_travel_cost()