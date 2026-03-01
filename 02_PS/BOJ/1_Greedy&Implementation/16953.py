import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_operations_a_to_b() -> None:
    start, target = map(int, input().split())
    operation_count = 0
    current = target
    
    # 그리디: B에서 A로 "역연산"으로 줄여 나가기
    while current > start:
        # 끝자리가 1이면, 오른쪽에 1 제거
        if current % 10 == 1:
            current //= 10
            operation_count +=1
        # 짝수면 2로 나누기
        elif current % 2 == 0:
            current //= 2
            operation_count += 1
        else:
            output(str(-1))
            return
        
    # 종확히 A에 도닳해야 성공
    if current == start:
        output(str(operation_count + 1))
    else:
        output(str(-1))
        
min_operations_a_to_b()