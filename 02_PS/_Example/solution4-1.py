# 정방행렬의 크기 N 입력 받기
N = int(input())

# 여행가 계획서 입력 받기
plans = input().split()

# 초기 위치 정의
x, y = 1, 1

# L, R, U, D 이동 방향 정의 
move_types = ['L', 'R', 'U', 'D']

# 이동 방향에 대한 좌표값 업데이트 지표 정의
dx = [0, 0 , -1, 1]
dy = [-1, 1, 0, 0]

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 예외 처리: 공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)