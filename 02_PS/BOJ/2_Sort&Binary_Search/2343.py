import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_bluray_size() -> None:
    lecture_count, bluray_count = map(int, input().split())
    lecture_lengths = list(map(int, input().split()))

    # 블루레이 크기는 적어도 가장 긴 강의 길이 이상이어야 함
    left = max(lecture_lengths)
    # 최악의 경우 전부 하나에 담는 크기
    right = sum(lecture_lengths)

    answer = right

    def required_blurays(bluray_size: int) -> int:
        count = 1
        current_sum = 0

        for length in lecture_lengths:
            if current_sum + length > bluray_size:
                count += 1
                current_sum = length
            else:
                current_sum += length

        return count

    while left <= right:
        mid = (left + right) // 2

        if required_blurays(mid) <= bluray_count:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    output(str(answer))

min_bluray_size()