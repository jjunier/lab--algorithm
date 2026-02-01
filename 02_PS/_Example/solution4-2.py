# 종료 시각(시)의 상한값 N 입력 (1 <= N <= 23): 시간 데드라인 설정
N = int(input())

# 숫자 '3'이 포함된 시각의 개수
num_count = 0

# 00:00:00 ~ N:59:59까지 모든 시각을 순회
for i in range(N + 1):          # 시 (Hour)
    for j in range(60):         # 분 (Minute)
        for k in range(60):     # 초 (Second)
            # 시, 분, 초 중에 하나라도 '3'이 포함되면 카운트하기
            if '3' in str(i) + str(j) + str(k):
                num_count += 1

print(num_count)