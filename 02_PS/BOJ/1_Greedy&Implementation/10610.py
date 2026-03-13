import sys

input = sys.stdin.readline
output = sys.stdout.write

def make_largest_multiple_of_30() -> None:
    number = input().strip()
    digits = list(number)
    
    # 0이 없으면 10의 배수가 될 수 없음
    if '0' not in digits:
        print(-1)
        return
    
    # 자리수 합이 3의 배수가 아니면 30의 배수가 될 수 없음
    digit_sum = sum(int(digit) for digit in digits)
    
    if digit_sum % 3 != 0:
        print(-1)
        return
    
    # 가장 큰 수를 만들기 위해 내림차순 정렬
    digits.sort(reverse=True)
    output("".join(digits))
    
make_largest_multiple_of_30()