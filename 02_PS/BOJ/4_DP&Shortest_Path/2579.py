import sys

input = sys.stdin.readline
output = sys.stdout.write

def max_stair_score() -> None:
    stair_count = int(input().strip())
    stair_score = [0] + [int(input().strip()) for _ in range(stair_count)]
    
    # dp[i] = i번째 계단을 반드시 밟고 도착하였을 때 얻을 수 있는 최대치의 점수
    dp = [0] * (stair_count + 1)
    dp[1] = stair_score[1]
    
    if stair_count >= 2:
        dp[2] = stair_score[1] + stair_score[2]
        
    for i in range(3, stair_count + 1):
        # Case 1: i-2 -> i 로 점프
        case_1 = dp[i - 2] + stair_score[i]
        
        # Case 2: i-3 -> i-1 -> i 순으로 점프
        case_2 = dp[i - 3] + stair_score[i - 1] + stair_score[i]
        
        dp[i] = max(case_1, case_2)
        
    output(str(dp[stair_count]))
    
max_stair_score()