import sys

input = sys.stdin.readline
output = sys.stdout.write

def print_bulk_ranks() -> None:
    person_count = int(input().strip())
    people = [tuple(map(int, input().split())) for _ in range(person_count)]

    ranks = [1] * person_count

    for current_idx in range(person_count):
        current_weight, current_height = people[current_idx]

        for other_idx in range(person_count):
            if current_idx == other_idx:
                continue

            other_weight, other_height = people[other_idx]

            # 다른 사람이 몸무게와 키 모두 더 크면
            # 현재 사람의 등수는 1 증가
            if other_weight > current_weight and other_height > current_height:
                ranks[current_idx] += 1

    output(" ".join(map(str, ranks)))

print_bulk_ranks()