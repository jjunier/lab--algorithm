import sys

input = sys.stdin.readline
output = sys.stdout.write

def max_lan_length() -> None:
    cable_count, required_count = map(int, input().split())
    cable_lengths = [int(input()) for _ in range(cable_count)]
    
    low_length = 1
    high_length = max(cable_lengths)
    best_length = 0
    
    while low_length <= high_length:
        made_length = 0
        mid_length = (low_length + high_length) // 2
        
        for length in cable_lengths:
            made_length += length // mid_length
        
        if made_length >= required_count:
            best_length = mid_length
            low_length = mid_length + 1
        else:
            high_length = mid_length - 1
            
    output(str(best_length))
        
max_lan_length()