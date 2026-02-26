import sys

input = sys.stdin.readline
output = sys.stdout.write

def count_fibonacci_zero_one() -> None:
    count_test_case = int(input().strip())
    targets = [int(input().strip()) for _ in range(count_test_case)]
    max_target = max(targets)
    
    # dp[n] = (zero_count, one_count)
    dp = [(0, 0)] * (max_target + 1)
    
    if max_target >= 0:
        dp[0] = (1, 0)
    if max_target >= 1:
        dp[1] = (0, 1)
        
    for value in range(2, max_target + 1):
        count_zero = dp[value - 1][0] + dp[value - 2][0]
        count_one = dp[value - 1][1] + dp[value - 2][1]
        dp[value] = (count_zero, count_one)
        
    for n in targets:
        print(dp[n][0], dp[n][1])

count_fibonacci_zero_one()