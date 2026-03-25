import sys
from collections import deque

input = sys.stdin.readline


def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    log = n.bit_length()
    parent = [[0] * (n + 1) for _ in range(log)]
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)

    q = deque([1])
    visited[1] = True

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                depth[nxt] = depth[cur] + 1
                parent[0][nxt] = cur
                q.append(nxt)

    for k in range(1, log):
        for v in range(1, n + 1):
            parent[k][v] = parent[k - 1][parent[k - 1][v]]

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a

        diff = depth[a] - depth[b]
        for k in range(log):
            if diff & (1 << k):
                a = parent[k][a]

        if a == b:
            return a

        for k in range(log - 1, -1, -1):
            if parent[k][a] != parent[k][b]:
                a = parent[k][a]
                b = parent[k][b]

        return parent[0][a]

    m = int(input())
    out = []
    for _ in range(m):
        a, b = map(int, input().split())
        out.append(str(lca(a, b)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()