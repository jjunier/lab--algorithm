def solution(arrows):
    directions = [
        (0, 1),    # 0
        (1, 1),    # 1
        (1, 0),    # 2
        (1, -1),   # 3
        (0, -1),   # 4
        (-1, -1),  # 5
        (-1, 0),   # 6
        (-1, 1)    # 7
    ]

    visited_node = set()
    visited_edge = set()

    x, y = 0, 0
    visited_node.add((x, y))
    answer = 0

    for arrow in arrows:
        dx, dy = directions[arrow]

        # 대각선 교차 처리를 위해 한 칸을 2번 나눠 이동
        for _ in range(2):
            nx, ny = x + dx, y + dy
            edge = ((x, y), (nx, ny))
            reverse_edge = ((nx, ny), (x, y))

            # 이미 방문한 정점이지만, 처음 지나는 간선이면 방 생성
            if (nx, ny) in visited_node and edge not in visited_edge:
                answer += 1

            visited_node.add((nx, ny))
            visited_edge.add(edge)
            visited_edge.add(reverse_edge)

            x, y = nx, ny

    return answer