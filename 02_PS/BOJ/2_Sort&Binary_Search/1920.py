import sys

def check_num_existence(numbers: set[int], queries: list[int]) -> str:
    output = []

    for q in queries:
        output.append("1" if q in numbers else "0")

    return "\n".join(output)

input = sys.stdin.readline

n = int(input().strip())
number_set = set(map(int, input().split()))

m = int(input().strip())
query_list = list(map(int, input().split()))

sys.stdout.write(check_num_existence(number_set, query_list))