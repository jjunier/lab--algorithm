import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
output = sys.stdout.write

def print_preorder_from_inorder_postorder() -> None:
    node_count = int(input().strip())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    # 값 -> inorder 인덱스
    inorder_index = [0] * (node_count + 1)
    for idx, value in enumerate(inorder):
        inorder_index[value] = idx

    preorder_result = []

    def build_preorder(
        inorder_start: int,
        inorder_end: int,
        postorder_start: int,
        postorder_end: int
    ) -> None:
        if inorder_start > inorder_end or postorder_start > postorder_end:
            return

        root = postorder[postorder_end]
        preorder_result.append(str(root))

        root_idx = inorder_index[root]
        left_size = root_idx - inorder_start

        # 왼쪽 서브트리
        build_preorder(
            inorder_start,
            root_idx - 1,
            postorder_start,
            postorder_start + left_size - 1
        )

        # 오른쪽 서브트리
        build_preorder(
            root_idx + 1,
            inorder_end,
            postorder_start + left_size,
            postorder_end - 1
        )

    build_preorder(0, node_count - 1, 0, node_count - 1)
    output(" ".join(preorder_result))

print_preorder_from_inorder_postorder()