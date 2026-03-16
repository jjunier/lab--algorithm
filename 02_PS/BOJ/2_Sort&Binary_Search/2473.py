import sys

input = sys.stdin.readline

def find_three_solutions() -> None:
    liquid_count = int(input().strip())
    liquids = list(map(int, input().split()))
    liquids.sort()

    best_abs_sum = float("inf")
    best_triplet = (0, 0, 0)

    for fixed_idx in range(liquid_count - 2):
        left = fixed_idx + 1
        right = liquid_count - 1

        while left < right:
            current_sum = liquids[fixed_idx] + liquids[left] + liquids[right]

            if abs(current_sum) < best_abs_sum:
                best_abs_sum = abs(current_sum)
                best_triplet = (
                    liquids[fixed_idx],
                    liquids[left],
                    liquids[right]
                )

            if current_sum > 0:
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                print(*best_triplet)
                return

    print(*best_triplet)

find_three_solutions()