import sys
from bisect import bisect_left

input = sys.stdin.readline

def lis_length() -> None:
    sequence_length = int(input().strip())
    sequence = list(map(int, input().split()))

    # lis_end_values[i]: 길이가 i+1인 증가 부분 수열들 중 마지막 값이 가장 작도록 유지한 값
    lis_end_values = []

    for value in sequence:
        insert_position = bisect_left(lis_end_values, value)

        if insert_position == len(lis_end_values):
            lis_end_values.append(value)
        else:
            lis_end_values[insert_position] = value

    print(len(lis_end_values))

lis_length()