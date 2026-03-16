import sys

input = sys.stdin.readline

def closest_solution() -> None:
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    # 두 포인터를 위해 정렬
    arr.sort()
    left = 0
    right = n - 1
    best_sum = float('inf')
    answer_left = 0 
    answer_right = 0
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        # 현재 합이 0에 더 가까우면 정답 갱신
        if abs(current_sum) < best_sum:
            best_sum = abs(current_sum)
            answer_left = arr[left]
            answer_right = arr[right]
            
        # 합이 0보다 크면 값을 줄이기 위해 오른쪽 포인터 이동
        if current_sum > 0:
            right -= 1
            
        # 합이 0보다 작으면 값을 키우기 위해 왼쪽 포인터 이동
        else:
            left += 1
            
    print(answer_left, answer_right)
    
closest_solution()