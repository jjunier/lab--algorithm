import sys

input = sys.stdin.readline
output = sys.stdout.write

def statistics() -> None:
    count = int(input().strip())
    numbers = [int(input().strip()) for _ in range(count)]
    numbers.sort()

    # 1) 산술평균 (반올림)
    mean = int(round(sum(numbers) / count))

    # 2) 중앙값
    median = numbers[count // 2]

    # 3) 최빈값 (여러 개면 두 번째로 작은 값)
    # 값 범위: -4000..4000 → 8001칸 카운팅
    offset = 4000
    freq = [0] * 8001
    for x in numbers:
        freq[x + offset] += 1

    max_freq = max(freq)
    modes = []
    for idx, f in enumerate(freq):
        if f == max_freq:
            modes.append(idx - offset)

    mode = modes[0] if len(modes) == 1 else modes[1]

    # 4) 범위
    value_range = numbers[-1] - numbers[0]

    output("\n".join(map(str, [mean, median, mode, value_range])))

statistics()