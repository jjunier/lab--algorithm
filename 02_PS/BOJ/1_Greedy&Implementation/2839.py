def sugar_pack_count(n):
    # 배달할 봉지 갯수 정의
    count = 0
    
    while n >= 0:
        if n % 5 == 0:
            count += n // 5
            return count
        else:
            n -= 3
            count += 1
    return -1

# 배달할 설탕 N 킬로그램 입력 받기
n = int(input())
print(sugar_pack_count(n))