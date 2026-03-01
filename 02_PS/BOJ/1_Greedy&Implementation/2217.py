import sys

input = sys.stdin.readline
output = sys.stdout.write

def max_lift_weight() -> None:
    rope_count = int(input().strip())
    rope_limits = [int(input().strip()) for _ in range(rope_count)]
    
    # 가장 약한 로프가 병렬 사용 시 한계가 되므로 오름차순 정렬
    rope_limits.sort()
    best = 0
    
    for i, limit in enumerate(rope_limits):
        used_rope_count  = rope_count - i
        best = max(best, limit * used_rope_count)
        
    output(str(best))
    
max_lift_weight()