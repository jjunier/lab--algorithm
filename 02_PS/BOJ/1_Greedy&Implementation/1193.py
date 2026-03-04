import sys

input = sys.stdin.readline
output = sys.stdout.write

def find_fraction() -> None:
    x = int(input().strip())
    diagonal = 1
    cumulative = 0
    
    # 어떤 대각선인지 찾기
    while cumulative + diagonal < x:
        cumulative += diagonal
        diagonal += 1
        
    position  = x - cumulative
    
    if diagonal % 2 == 0:
        numerator = position
        denominator = diagonal - position + 1
    else:
        numerator = diagonal - position + 1
        denominator = position
        
    output(str(f"{numerator}/{denominator}"))
    
find_fraction()