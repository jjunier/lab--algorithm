import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_flip_count() -> None:
    binary_string = input().strip()
    zero_group = 0
    one_group = 0

    # 첫 문자 기준 그룹 시작
    if binary_string[0] == '0':
        zero_group += 1
    else:
        one_group += 1

    # 이전 문자와 다르면 새로운 그룹 시작
    for idx in range(1, len(binary_string)):
        if binary_string[idx] != binary_string[idx - 1]:
            if binary_string[idx] == '0':
                zero_group += 1
            else:
                one_group += 1

    output(str(min(zero_group, one_group)))

min_flip_count()