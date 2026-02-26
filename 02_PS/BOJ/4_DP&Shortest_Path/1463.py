import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_operations_to_one() -> None:
    target = int(input().strip())
    
    # dp[i] = i를 1로 만드는 최소 연산 횟수
    dp = [0] * (target + 1)
    
    for value in range(2, target + 1):
        # Case 1: 1을 빼는 경우
        dp[value] = dp[value - 1] + 1
        
        # Case 2: 2로 나누는 경우
        if value % 2 == 0:
            dp[value] = min(dp[value], dp[value // 2] + 1)
            
        # Case 3: 3으로 나누는 경우
        if value % 3 == 0:
            dp[value] = min(dp[value], dp[value // 3] + 1)
    
    output(str(dp[target]))
    
min_operations_to_one()