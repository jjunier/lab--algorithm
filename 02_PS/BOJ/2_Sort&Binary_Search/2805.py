import sys

input = sys.stdin.readline
output = sys.stdout.write

def max_cutter_height() -> None:
    tree_count, required_wood = map(int, input().split())
    tree_heights = list(map(int, input().split()))
    
    low_height = 0
    high_height = max(tree_heights)
    best_height = 0
    
    while low_height <= high_height:
        collected_wood = 0
        mid_height = (low_height + high_height) // 2
        
        for height in tree_heights:
            if height > mid_height:
                collected_wood += (height - mid_height)
                
        if collected_wood >= required_wood:
            best_height = mid_height
            low_height = mid_height + 1
        else:
            high_height = mid_height - 1
            
    output(str(best_height))
    
max_cutter_height()