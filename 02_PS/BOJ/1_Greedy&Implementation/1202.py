import sys
import heapq

input = sys.stdin.readline

def steal_jewels() -> None:
    jewel_count, bag_count = map(int, input().split())

    jewels = [tuple(map(int, input().split())) for _ in range(jewel_count)]
    bags = [int(input()) for _ in range(bag_count)]

    # 보석: 무게 기준 정렬
    jewels.sort()

    # 가방: 작은 가방부터
    bags.sort()

    max_heap = [] 
    total_value = 0
    jewel_index = 0

    for bag_capacity in bags:

        # 현재 가방에 들어갈 수 있는 보석 전부 후보에 넣기
        while jewel_index < jewel_count and jewels[jewel_index][0] <= bag_capacity:
            weight, value = jewels[jewel_index]
            heapq.heappush(max_heap, -value)  # 최대 힙
            jewel_index += 1

        # 후보 중 가장 비싼 보석 선택
        if max_heap:
            total_value += -heapq.heappop(max_heap)

    print(total_value)

steal_jewels()