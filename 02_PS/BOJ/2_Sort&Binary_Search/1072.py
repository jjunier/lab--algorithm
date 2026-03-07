import sys

input = sys.stdin.readline
output = sys.stdout.write

def min_games_to_change_win_rate() -> None:
    total_games, won_games = map(int, input().split())

    current_rate = (won_games * 100) // total_games

    # 승률이 99 이상이면 더 이겨도 정수 승률이 변하지 않음
    if current_rate >= 99:
        output(str(-1))
        return

    left = 1
    right = 1_000_000_000
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        new_rate = ((won_games + mid) * 100) // (total_games + mid)

        if new_rate > current_rate:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    output(str(answer))

min_games_to_change_win_rate()