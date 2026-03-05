import sys

input = sys.stdin.readline
output = sys.stdout.write

def coordinate_compress() -> None:
    count = int(input().strip())
    values = list(map(int, input().split()))
    
    # 중복 제거 후 정렬하기
    sorted_unique = sorted(set(values))
    
    # 값 -> 압축 좌표(순위) 매핑하기
    rank_by_value = {value: rank for rank, value in enumerate(sorted_unique)}
    
    # 원래 순서대로 출력하기
    compressed = [str(rank_by_value[v]) for v in values]
    output(" ".join(compressed))
    
coordinate_compress()