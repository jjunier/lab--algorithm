import sys

input = sys.stdin.readline
output = sys.stdout.write

def check_numbers_in_note() -> None:
    test_case_count = int(input().strip())
    output_lines = []

    for _ in range(test_case_count):
        note1_count = int(input().strip())
        note1_numbers = set(map(int, input().split()))

        note2_count = int(input().strip())
        note2_numbers = list(map(int, input().split()))

        for number in note2_numbers:
            output_lines.append("1" if number in note1_numbers else "0")

    output("\n".join(output_lines))

check_numbers_in_note()