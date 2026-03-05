import sys

input = sys.stdin.readline
output = sys.stdout.write

def digits_descending_sort() -> None:
    number = input().strip()
    digits = sorted(number, reverse=True)

    output("".join(digits))

digits_descending_sort()
