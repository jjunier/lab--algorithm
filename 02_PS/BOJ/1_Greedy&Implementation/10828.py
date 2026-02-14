import sys

def run_stack_commands(command_count: int) -> None:
    stack: list[int] = []
    output: list[str] = []
    
    for _ in range(command_count):
        command = sys.stdin.readline().split()
        
        if command[0] == "push":
            stack.append(int(command[1]))
            
        elif command[0] == "pop":
            output.append(str(stack.pop() if stack else -1))
            
        elif command[0] == "size":
            output.append(str(len(stack)))
            
        elif command[0] == "empty":
            output.append("1" if not stack else "0")
            
        elif command[0] == "top":
            output.append(str(stack[-1] if stack else -1))
        
    sys.stdout.write("\n".join(output))
            
n = int(sys.stdin.readline())
run_stack_commands(n)