import sys

input = sys.stdin.readline
output = sys.stdout.write

def max_distinct_natural_count() -> None:
    total = int(input().strip())
    count = 0
    current = 1
    remaining = total
    
    # 1, 2, 3, ... 처럼 가장 작은 수부터 골라야 N이 최대가 됨
    while remaining >= current:
        remaining -= current
        count += 1
        current += 1
        
    output(str(count))
    
max_distinct_natural_count()