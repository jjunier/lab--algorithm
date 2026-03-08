import sys

input = sys.stdin.readline
output = sys.stdout.write

def check_phone_list() -> None:
    test_case_count = int(input().strip())
    
    for _ in range(test_case_count):
        phone_count = int(input().strip())
        phone_numbers = [input().strip() for _ in range(phone_count)]
        
        # 사전순으로 정렬
        phone_numbers.sort()
        is_consistent = True
        
        # 인접한 번호만 확인하기
        for i in range(phone_count - 1):
            if phone_numbers[i + 1].startswith(phone_numbers[i]):
                is_consistent = False
                break
                
        if is_consistent:
            output("YES\n")
        else:
            output("NO\n")
            
check_phone_list()   