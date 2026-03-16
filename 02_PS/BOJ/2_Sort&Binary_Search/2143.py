import sys
from collections import Counter

input = sys.stdin.readline

def count_subarray_sum_pairs() -> None:
    target_sum = int(input().strip())

    a_length = int(input().strip())
    a = list(map(int, input().split()))

    b_length = int(input().strip())
    b = list(map(int, input().split()))

    # A의 모든 부배열 합 구하기
    a_sub_sums = []
    for start_idx in range(a_length):
        current_sum = 0
        for end_idx in range(start_idx, a_length):
            current_sum += a[end_idx]
            a_sub_sums.append(current_sum)

    # B의 모든 부배열 합 구하기
    b_sub_sums = []
    for start_idx in range(b_length):
        current_sum = 0
        for end_idx in range(start_idx, b_length):
            current_sum += b[end_idx]
            b_sub_sums.append(current_sum)

    # B의 부배열 합 개수 세기
    b_sum_count = Counter(b_sub_sums)

    answer = 0
    for a_sum in a_sub_sums:
        answer += b_sum_count[target_sum - a_sum]

    print(answer)

count_subarray_sum_pairs()