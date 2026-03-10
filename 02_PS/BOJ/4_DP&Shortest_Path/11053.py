import sys

input = sys.stdin.readline
output = sys.stdout.write

def logest_increasing_subsequence() -> None:
    number_count = int(input().strip())
    sequence = list(map(int, input().split()))

    # dp[i] = i번째 원소를 마지막으로 하는 LIS 길이
    dp = [1] * number_count

    for current_idx in range(number_count):
        for prev_idx in range(current_idx):
            if sequence[prev_idx] < sequence[current_idx]:
                dp[current_idx] = max(dp[current_idx], dp[prev_idx] + 1)

    output(str(max(dp)))

logest_increasing_subsequence()