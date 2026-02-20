import sys

def sort_numbers(count: int) -> None:
    numbers = [int(sys.stdin.readline()) for _ in range(count)]

    # N개의 수 오름차순으로 정렬 (sort(): Timesort (O(N log N)))
    numbers.sort()

    sys.stdout.write("\n".join(map(str, numbers)))

n = int(sys.stdin.readline())
sort_numbers(n)