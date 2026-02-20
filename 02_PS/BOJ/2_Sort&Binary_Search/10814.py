import sys

input = sys.stdin.readline
output = sys.stdout.write

def sort_members(member_count: int) -> None:
    members: list[tuple[int, int, str]]  = []

    for join_order in range(member_count):
        age_str, name = input().split()
        age = int(age_str)
        members.append((age, join_order, name))

    # 나이를 기준으로 오름차순 정렬, 만약 나이가 같은 경우 가입순으로 정렬
    members.sort(key=lambda m: (m[0], m[1]))

    output("\n".join(f"{age} {name}" for age, _, name in members))

n = int(input().strip())
sort_members(n)