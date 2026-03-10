import sys

input = sys.stdin.readline
output = sys.stdout.write

def count_bridge_cases() -> None:
    test_case_count = int(input().strip())
    results = []

    for _ in range(test_case_count):
        west_count, east_count = map(int, input().split())

        # 서쪽 N개를 동쪽 N개 중 어디에 놓을 지 고르는 조합과 같음
        result = 1

        for i in range(1, west_count + 1):
            result = result * (east_count - i + 1) // i

        results.append(str(result))

    output("\n".join(results))

count_bridge_cases()