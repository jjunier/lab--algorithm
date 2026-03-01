import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_scalar_product() -> None:
    n = int(input().strip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # S 최소화: A는 오름차순, B는 내림차순 (값 기준으로 매칭)
    a.sort()
    b.sort(reverse=True)
    result = 0
    
    for i in range(n):
        result += a[i] * b[i]
        
    output(str(result))
    
min_scalar_product()