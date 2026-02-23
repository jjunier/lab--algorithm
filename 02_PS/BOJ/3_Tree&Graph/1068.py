import sys

input = sys.stdin.readline
output = sys.stdout.write

def count_leaf_node() -> None:
    node_count = int(input().strip())
    parent = list(map(int, input().split()))
    delete_node = int(input().strip())
    
    children = [[] for _ in range(node_count)]
    root = -1
    
    for node, parent_node in enumerate(parent):
        if parent_node == -1:
            root = node
        else:
            children[parent_node].append(node)
            
    def count_leaves(node: int) -> int:
        # 삭제된 노드(혹은 그 하위 트리)는 남은 트리에 반영하지 않음
        if node == delete_node:
            return 0
        
        alive_child_count = 0
        leaf_total = 0
        
        for child in children[node]:
            # 삭제 노드를 자식으로 가진 경우엔, 카운트하지 않음
            if child != delete_node:
                alive_child_count += 1
                
            leaf_total += count_leaves(child)
            
        # 살아있는 자식 노드가 없는 경우 현재 노드는 리프
        return 1 if alive_child_count == 0 else leaf_total
    
    # 루트가 삭제되는 경우엔, 남는 리프 노드 없음
    if root == delete_node:
        output(str(0))
    else:
        output(str(count_leaves(root)))
    
count_leaf_node()