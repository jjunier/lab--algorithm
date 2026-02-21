import sys

input = sys.stdin.readline
output = sys.stdout.write

def check_number_cards() -> None:
    n = input()
    card_set = set(map(int, input().split()))

    m = input()
    queries = map(int, input().split())

    output(" ".join("1" if q in card_set else "0" for q in queries))

check_number_cards()