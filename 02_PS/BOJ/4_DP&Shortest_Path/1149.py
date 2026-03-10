import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_rgb_paint_cost() -> None:
    house_count = int(input().strip())
    costs = [list(map(int, input().split())) for _ in range(house_count)]

    # dp[i][color] = i번째 집까지 칠했을 경우, i번째 집을 color로 칠하는 최소 비용
    dp = [[0] * 3 for _ in range(house_count)]

    # 첫 번째 집 초기화
    dp[0][0] = costs[0][0]  # 빨강
    dp[0][1] = costs[0][1]  # 초록
    dp[0][2] = costs[0][2]  # 파랑

    for house_idx in range(1, house_count):
        # 현재 집을 빨강으로 칠하면 이전 집은 초록/파랑만 가능
        dp[house_idx][0] = min(dp[house_idx - 1][1], dp[house_idx - 1][2]) + costs[house_idx][0]
        # 현재 집을 초록으로 칠하면 이전 집은 빨강/파랑만 가능
        dp[house_idx][1] = min(dp[house_idx - 1][0], dp[house_idx - 1][2]) + costs[house_idx][1]
        # 현재 집을 파랑으로 칠하면 이전 집은 빨강/초록만 가능
        dp[house_idx][2] = min(dp[house_idx - 1][0], dp[house_idx - 1][1]) + costs[house_idx][2]

    output(str(min(dp[house_count - 1])))

min_rgb_paint_cost()