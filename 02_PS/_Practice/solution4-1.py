# 기사의 위치 입력 받기
knight_loc = input()

# 체스판 좌표 정의하기
dx = int(knight_loc[1])                              # 행(row)
# ord 함수: 주어진 문자의 유니코드(Unicode) 코드 포인트(정수 값)를 반환하는 함수
dy = int(ord(knight_loc[0])) - int(ord('a')) + 1     # 열(col)

# 나이트가 이동 가능한 방향 8가지 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 결과 정의
count = 0

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인

for step in steps:
    # 이동하고자 하는 위치 확인
    next_dx = dx + step[0]
    next_dy = dy + step[1]

    if next_dx >= 1 and next_dx <= 8 and next_dy >= 1 and next_dy <= 8:
        count += 1

print(count)