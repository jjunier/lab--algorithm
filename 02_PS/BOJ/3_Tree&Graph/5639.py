import sys

input = sys.stdin.readline
output = sys.stdout.write
sys.setrecursionlimit(10**6)

def print_postorder_from_preorder() -> None:
    preorder = []
    
    while True:
        line = input().strip()
        
        if not line:
            break
        preorder.append(int(line))
        
    output_lines = []
    
    def build_postorder(start_idx: int, end_idx: int) -> None:
        if start_idx >= end_idx:
            return 
        
        root_value = preorder[start_idx]
        split_idx = start_idx + 1
        
        while split_idx < end_idx and preorder[split_idx] < root_value:
            split_idx += 1
            
        # 왼쪽 서브트리
        build_postorder(start_idx + 1, split_idx)
        
        # 오른쪽 서브트리
        build_postorder(split_idx, end_idx)
        
        # 루트
        output_lines.append(str(root_value))
        
    build_postorder(0, len(preorder))
    output("\n".join(output_lines))
    
print_postorder_from_preorder()