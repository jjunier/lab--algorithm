import sys

output = sys.stdout.write

def print_self_numbers_up_to_10000() -> None:
    limit = 10000
    generated = [False] * (limit + 1)
    
    def d(n: int) -> int:
        total = n
        
        while n > 0:
            total += n % 10
            n //= 10
            
        return total
    
    for n in range(1, limit + 1):
        g = d(n)
        
        if g <= limit:
            generated[g] = True
            
    out_lines = []
    
    for n in range(1, limit + 1):
        if not generated[n]:
            out_lines.append(str(n))
            
    output("\n".join(out_lines))

print_self_numbers_up_to_10000()