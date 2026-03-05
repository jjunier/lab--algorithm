import sys

input = sys.stdin.readline
output = sys.stdout.write

def axis_sort_by_y() -> None:
    point_count = int(input().strip())
    points = [tuple(map(int, input().split())) for _ in range(point_count)]

    # y를 기준으로 오름차순 (만약 y가 같은 경우 x를 기준으로 오름차순)
    points.sort(key=lambda p: [p[1], p[0]])
    out_lines = [f"{x} {y}" for x, y in points]

    output("\n".join(out_lines))

axis_sort_by_y()