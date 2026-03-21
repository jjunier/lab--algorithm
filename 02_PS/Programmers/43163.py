from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    def can_change(word1, word2):
        diff = 0
        for a, b in zip(word1, word2):
            if a != b:
                diff += 1
        return diff == 1

    queue = deque([(begin, 0)])
    visited = set([begin])

    while queue:
        current, count = queue.popleft()

        if current == target:
            return count

        for word in words:
            if word not in visited and can_change(current, word):
                visited.add(word)
                queue.append((word, count + 1))

    return 0