import sys
from functools import reduce

input = sys.stdin.readline


def solve():
    n = int(input())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 1을 루트로 하는 트리 구성
    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1

    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)

    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)

    # 후위 순회처럼 역순 처리
    for u in reversed(order):
        children = tuple(filter(lambda v: v != parent[u], graph[u]))

        dp0[u] = reduce(
            lambda acc, v: acc + dp1[v],
            children,
            0
        )

        dp1[u] = 1 + reduce(
            lambda acc, v: acc + min(dp0[v], dp1[v]),
            children,
            0
        )

    print(min(dp0[1], dp1[1]))


if __name__ == "__main__":
    solve()