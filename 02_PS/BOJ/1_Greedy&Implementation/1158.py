import sys
from collections import deque

input = sys.stdin.readline

def josephus_sequence() -> None:
    person_count, step = map(int, input().split())

    people = deque(range(1, person_count + 1))
    result = []

    while people:
        # K번째 사람이 맨 앞으로 오도록 회전
        people.rotate(-(step - 1))
        result.append(str(people.popleft()))

    print("<" + ", ".join(result) + ">")

josephus_sequence()