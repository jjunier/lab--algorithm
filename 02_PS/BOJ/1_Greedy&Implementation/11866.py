import sys
from collections import deque

input = sys.stdin.readline

def josephus_sequence() -> None:
    person_count, step = map(int, input().split())

    people = deque(range(1, person_count + 1))
    result = []

    while people:
        # K번째 사람이 앞으로 오도록 회전
        people.rotate(-(step - 1))
        result.append(people.popleft())

    print("<" + ", ".join(map(str, result)) + ">")

josephus_sequence()