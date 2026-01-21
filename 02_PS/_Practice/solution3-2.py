# 카드의 행(N)과 열(M)을 담당하는 수 입력 받기
N, M = map(int, input().split())

answer = 0

for i in range(N):
    # 입력 받은 자연수를 저장하는 리스트 data 변수
    data = list(map(int, input().split()))

    # 리스트 data 변수 내에서 최솟값을 찾아 저장
    min_num_in_data = min(data)

    # answer에 저장된 값과 리스트 data에서 찾은 최솟값을 비교하여 더 큰 값을 저장
    answer = max(answer, min_num_in_data)

print(answer)