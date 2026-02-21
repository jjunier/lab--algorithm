import sys
from collections import Counter

input = sys.stdin.readline
output = sys.stdout.write

def count_number_cards() -> None:
    card_count = Counter(map(int, input().split()))
    m = input()
    queries = map(int, input().split())
    
    result = (str(card_count[q]) for q in queries)
    output(" ".join(result))
    
n = input()
count_number_cards()