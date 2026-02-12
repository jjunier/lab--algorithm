import sys

def min_expression_value(expression: str) -> int:
    # '-'을 기준으로 분리함
    parts = expression.split('-')
    total = sum(map(int, parts[0].split('+')))
    
    for part in parts[1:]:
        total -= sum(map(int, part.split('+')))
    
    return total
    
expr = sys.stdin.readline().strip()

print(min_expression_value(expr))