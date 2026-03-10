import sys

input = sys.stdin.readline
output = sys.stdout.write

def max_triangle_sum() -> None:
    triangle_size = int(input().strip())
    triangle = [list(map(int, input().split())) for _ in range(triangle_size)]

    # dp[row][col] = (row, col)까지 왔을 때의 최대 합
    dp = [row[:] for row in triangle]

    for row in range(1, triangle_size):
        for col in range(row + 1):
            # 맨 왼쪽: 바로 위 오른쪽 부모만 가능
            if col == 0:
                dp[row][col] += dp[row - 1][col]
            # 맨 오른쪽: 바로 위 왼쪽 부모만 가능
            elif col == row:
                dp[row][col] += dp[row - 1][col - 1]
            # 가운데: 위 왼쪽 / 위 오른쪽 중 큰 값 선택
            else:
                dp[row][col] += max(dp[row - 1][col - 1], dp[row - 1][col])

    output(str(max(dp[triangle_size - 1])))

max_triangle_sum()