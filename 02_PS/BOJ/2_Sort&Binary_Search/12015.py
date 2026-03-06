import sys
from bisect import bisect_left

input = sys.stdin.readline
output = sys.stdout.write

def lis_length() -> None:
    sequence_length = int(input().strip())
    sequence = list(map(int, input().split()))
    # lis[i]: 길이가 i+1인 증가 부분 수열 중 마지막 값이 가장 작도록 유지한 값
    lis = []

    for value in sequence:
        # value가 들어갈 가장 왼쪽 위치를 이진 탐색으로 찾기
        insert_pos = bisect_left(lis, value)

        # 현재 value가 lis의 모든 값보다 크면 되에 추가
        if insert_pos == len(lis):
            lis.append(value)
        else:
            # 기존 값을 더 작은 값으로 교체하여 이후 더 긴 증가 부분 수열을 만들 가능성을 남기기
            lis[insert_pos] = value

    # lis의 길이: 가장 긴 증가하는 부분 수열의 길이
    output(str(len(lis)))

lis_length()