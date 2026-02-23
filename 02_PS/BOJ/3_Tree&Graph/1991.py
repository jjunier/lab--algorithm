import sys

input = sys.stdin.readline
output = sys.stdout.write

def tree_traversals_result() -> None:
    node_count = int(input().strip())
    children: dict[str, tuple[str, str]] = {}

    for _ in range(node_count):
        node, left, right = input().split()
        children[node] = (left, right)

    def preorder(node: str, result: list[str]) -> None:
        if node == '.':
            return
        left, right = children[node]
        result.append(node)
        preorder(left, result)
        preorder(right, result)

    def inorder(node: str, result: list[str]) -> None:
        if node == '.':
            return
        left, right = children[node]
        inorder(left, result)
        result.append(node)
        inorder(right, result)

    def postorder(node: str, result: list[str]) -> None:
        if node == '.':
            return
        left, right = children[node]
        postorder(left, result)
        postorder(right, result)
        result.append(node)

    pre_result: list[str] = []
    in_result: list[str] = []
    post_result: list[str] = []

    preorder('A', pre_result)
    inorder('A', in_result)
    postorder('A', post_result)

    output("".join(pre_result) + "\n")
    output("".join(in_result) + "\n")
    output("".join(post_result) + "\n")

tree_traversals_result()