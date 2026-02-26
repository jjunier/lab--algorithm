import sys

input = sys.stdin.readline
output = sys.stdout.write

def count_ways_sum_123() -> None:
    test_case_count = int(input().strip())
    targets = [int(input().strip()) for _ in range(test_case_count)]
    max_target = max(targets)
    
    # dp[i] = i를 1,2,3의 합으로써 나타내는 방법의 수
    dp = [0] * (max_target + 1)
    
    if max_target >= 1:
        dp[1] = 1        # 1
    if max_target >= 2:
        dp[2] = 2        # 1+1, 2
    if max_target >= 3:
        dp[3] = 4        # 1+1+1, 1+2, 2+1, 3
        
    for value in range(4, max_target + 1):
        dp[value] = dp[value - 1] + dp[value - 2] + dp[value - 3]
        
    output("\n".join(str(dp[n]) for n in targets))
    
count_ways_sum_123()