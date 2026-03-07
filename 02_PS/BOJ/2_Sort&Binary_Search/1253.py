import sys

input = sys.stdin.readline

def count_good_numbers() -> None:
    number_count = int(input().strip())
    numbers = list(map(int, input().split()))
    numbers.sort()

    good_count = 0

    for target_idx in range(number_count):
        target_value = numbers[target_idx]

        left = 0
        right = number_count - 1

        while left < right:
            # 자기 자신을 사용하면 안 됨
            if left == target_idx:
                left += 1
                continue
            if right == target_idx:
                right -= 1
                continue

            current_sum = numbers[left] + numbers[right]

            if current_sum == target_value:
                good_count += 1
                break
            elif current_sum < target_value:
                left += 1
            else:
                right -= 1

    print(good_count)

count_good_numbers()