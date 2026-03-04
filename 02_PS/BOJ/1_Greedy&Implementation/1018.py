import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_repaint_for_chessboard() -> None:
    row_count, col_count = map(int, input().split())    # N, M
    board = [input().strip() for _ in range(row_count)]
    best = 64    # 최대 칠하기 수 (8 x 8)
    
    for start_row in range(row_count - 7):
        for start_col in range(col_count - 7):
            repaint_if_white_start = 0    # (start_row, start_col)이 'W'라고 가정
            repaint_if_black_start = 0    # (start_row, start_col)이 'B'라고 가정
            
            for r in range(8):
                for c in range(8):
                    current = board[start_row + r][start_col + c]
                    
                    # (r+c)가 짝수인 칸은 시작 색과 같아야 함
                    if (r+c) % 2 == 0:
                        if current != 'W':
                            repaint_if_white_start += 1
                        if current != 'B':
                            repaint_if_black_start += 1
                            
                    else:
                        # (r+c)가 홀수인 칸은 시작 색과 달라야 함
                        if current != 'B':
                            repaint_if_white_start += 1
                        if current != 'W':
                            repaint_if_black_start += 1
                        
            best = min(best, repaint_if_white_start, repaint_if_black_start)
            
    output(str(best))
    
min_repaint_for_chessboard()