# 자연수 N과 K에 대해서 입력 받기
N, K = map(int, input().split())

answer = 0

while True:
    target = (N // K) * K
    answer += (N - target)

    if N < K:
        break

    result += 1
    N //= K

result += (N - 1)
print(answer)
