import sys
from collections import deque

input = sys.stdin.readline

def run_deque_commands() -> None:
    command_count = int(input().strip())
    dq = deque()
    output_lines = []

    for _ in range(command_count):
        command = input().split()

        if command[0] == "push_front":
            dq.appendleft(int(command[1]))

        elif command[0] == "push_back":
            dq.append(int(command[1]))

        elif command[0] == "pop_front":
            output_lines.append(str(dq.popleft() if dq else -1))

        elif command[0] == "pop_back":
            output_lines.append(str(dq.pop() if dq else -1))

        elif command[0] == "size":
            output_lines.append(str(len(dq)))

        elif command[0] == "empty":
            output_lines.append("1" if not dq else "0")

        elif command[0] == "front":
            output_lines.append(str(dq[0] if dq else -1))

        elif command[0] == "back":
            output_lines.append(str(dq[-1] if dq else -1))

    sys.stdout.write("\n".join(output_lines))

run_deque_commands()