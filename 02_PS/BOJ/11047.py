import sys

def min_count_coins(n: int, k: int, coins: list[int]) -> int:
    count = 0
    
    # 오름차순으로 동전이 입력되므로 큰 동전부터 계산
    for coin in reversed(coins):
        if k == 0:
            break
        
        use = k // coin
        count += use
        k -= use * coin
    
    return count

input = sys.stdin.readline

coin_types, target_value = map(int, input().split())
coins = [int(input()) for _ in range(coin_types)]

print(min_count_coins(coin_types, target_value, coins))