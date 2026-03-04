import sys

input = sys.stdin.readline
output = sys.stdout.write

def calculate_sum() -> None:
    count = int(input().strip())
    stack = []
    
    for _ in range(count):
        number = int(input().strip())
        
        if number == 0:
            stack.pop()
        else:
            stack.append(number)
            
    output(str(sum(stack)))
    
calculate_sum()