import sys
from collections import deque

input = sys.stdin.readline


def solve():
    case_num = 1
    answers = []

    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)
        tree_count = 0

        for start in range(1, n + 1):
            if visited[start]:
                continue

            queue = deque([(start, 0)])
            visited[start] = True
            is_tree = True

            while queue:
                node, parent = queue.popleft()

                for nxt in graph[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        queue.append((nxt, node))
                    elif nxt != parent:
                        is_tree = False

            if is_tree:
                tree_count += 1

        if tree_count == 0:
            answers.append(f"Case {case_num}: No trees.")
        elif tree_count == 1:
            answers.append(f"Case {case_num}: There is one tree.")
        else:
            answers.append(f"Case {case_num}: A forest of {tree_count} trees.")

        case_num += 1

    print("\n".join(answers))


if __name__ == "__main__":
    solve()