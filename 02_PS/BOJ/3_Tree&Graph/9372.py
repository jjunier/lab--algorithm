import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_flight_types() -> None:
    test_case_count = int(input().strip())
    results = []
    
    for _ in range(test_case_count):
        country_count, flight_count = map(int, input().split())
        
        # 비행 스캐줄 입력은 읽기
        for _ in range(flight_count):
            input()
            
        results.append(str(country_count - 1))
        
    output("\n".join(results))
    
min_flight_types()