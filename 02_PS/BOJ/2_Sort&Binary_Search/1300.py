import sys

input = sys.stdin.readline
output = sys.stdout.write

def find_kth_number() -> None:
    size = int(input().strip())
    kth_index = int(input().strip())
    left = 1
    right = kth_index   # B[k]는 k를 넘지 않음
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        # mid 이하의 수가 곱셈표에 몇 개 있는지 계산
        count = 0

        for row in range(1, size + 1):
            count += min(mid // row, size)

        # mid 이하의 수가 k개 이상이면, 답이 될 수 있으므로 더 작은 값 탐색
        if count >= kth_index:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    output(str(answer))

find_kth_number()