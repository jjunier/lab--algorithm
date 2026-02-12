def calc(times):
    times.sort()
    total = 0
    acc = 0
    
    for time in times:
        acc += time
        total += acc
    
    return total

n = int(input())
usage_time = list(map(int, input().split()))

print(calc(usage_time))