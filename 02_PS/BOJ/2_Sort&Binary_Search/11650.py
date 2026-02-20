import sys

input = sys.stdin.readline
output = sys.stdout.write

def sort_coord_value(count: int) -> None:
    points = []

    for _ in range(count):
        x_coord, y_coord = map(int, input().split())
        points.append((x_coord, y_coord))

    # x좌표를 기준으로 오름차순 정렬, x좌표가 같은 경우엔 y좌표를 기준으로 정렬
    points.sort(key=lambda point: (point[0], point[1]))

    output("\n".join(f"{x} {y}" for x, y in points))

n = int(input().strip())
sort_coord_value(n)