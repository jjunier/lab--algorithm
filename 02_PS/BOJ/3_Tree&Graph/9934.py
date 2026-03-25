import sys

def solve():
    input = sys.stdin.readline

    k = int(input())
    inorder = list(map(int, input().split()))
    levels = [[] for _ in range(k)]

    def dfs(left, right, depth):
        if left > right:
            return
        mid = (left + right) // 2
        levels[depth].append(inorder[mid])
        dfs(left, mid - 1, depth + 1)
        dfs(mid + 1, right, depth + 1)

    dfs(0, len(inorder) - 1, 0)
    print("\n".join(" ".join(map(str, row)) for row in levels))

if __name__ == "__main__":
    solve()