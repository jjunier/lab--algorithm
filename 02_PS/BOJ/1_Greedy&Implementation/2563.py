import sys

input = sys.stdin.readline
output = sys.stdout.write

def black_area() -> None:
    paper_count = int(input().strip())

    # 100x100 도화지
    board = [[0] * 100 for _ in range(100)]

    for _ in range(paper_count):
        left, bottom = map(int, input().split())

        # 10x10 색종이 영역 칠하기
        for row in range(bottom, bottom + 10):
            for col in range(left, left + 10):
                board[row][col] = 1

    area = 0
    for row in range(100):
        area += sum(board[row])

    output(str(area))

black_area()