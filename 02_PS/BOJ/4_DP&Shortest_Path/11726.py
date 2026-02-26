import sys

input = sys.stdin.readline
output = sys.stdout.write

def count_tiling_2xn() -> None:
    width = int(input().strip())
    mod = 10007
    
    # dp[i] = 2xi를 채우는 방법의 수
    dp = [0] * (width + 1)
    dp[1] = 1
    
    if width >= 2:
        dp[2] = 2
        
    for i  in range(3, width + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
        
    output(str(dp[width] % mod))
    
count_tiling_2xn()