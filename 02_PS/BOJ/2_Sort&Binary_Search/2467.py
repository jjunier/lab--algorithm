import sys

input = sys.stdin.readline

def find_closet_to_zero() -> None:
    n = int(input().strip())
    liquids = list(map(int, input().split()))
    left = 0
    right = n -1 
    best_sum = float('inf')
    best_pair = (0, 0)
    
    while left < right:
        current_sum = liquids[left] + liquids[right]
        
        # 0에 더 가가우면 갱신
        if abs(current_sum) < abs(best_sum):
            best_sum = current_sum
            best_pair = (liquids[left], liquids[right])
            
        # 합이 양수이면 값을 줄이기 위해 오른쪽으로 이동하기
        if current_sum > 0:
            right -= 1
        else:
            left += 1
            
    print(best_pair[0], best_pair[1])
    
find_closet_to_zero()