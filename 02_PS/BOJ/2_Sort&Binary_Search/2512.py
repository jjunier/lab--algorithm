import sys

input = sys.stdin.readline

def max_budget_cap() -> None:
    region_count = int(input().strip())
    requests = list(map(int, input().split()))
    total_budget = int(input().strip())

    # 모든 요청을 그대로 배정 가능한 경우
    if sum(requests) <= total_budget:
        print(max(requests))
        return

    left = 0
    right = max(requests)
    best_cap = 0

    while left <= right:
        mid_cap = (left + right) // 2

        allocated = 0
        for request in requests:
            allocated += min(request, mid_cap)

        if allocated <= total_budget:
            best_cap = mid_cap
            left = mid_cap + 1
        else:
            right = mid_cap - 1

    print(best_cap)

max_budget_cap()