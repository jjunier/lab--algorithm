import sys

input = sys.stdin.readline
output = sys.stdout.write

def find_unknown_people() -> None:
    n, m = map(int, input().split())
    
    # 듣도 못한 사람
    unheard = set(input().strip() for _ in range(n))
    
    # 보도 못한 사람 중에서 듣도 못한 사람이 있는지 확인하기
    result = []

    for _ in range(m):
        name = input().strip()
        
        if name in unheard:
            result.append(name)
    
    # 사전 순으로 정렬하기
    result.sort()
    
    output(str(len(result)) + "\n")
    output("\n".join(result))
    
find_unknown_people()