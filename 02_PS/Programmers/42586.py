def solution(progresses, speeds):
    days = []

    for p, s in zip(progresses, speeds):
        remain = 100 - p
        days.append((remain + s - 1) // s)

    answer = []
    current = days[0]
    count = 1

    for day in days[1:]:
        if day <= current:
            count += 1
        else:
            answer.append(count)
            current = day
            count = 1

    answer.append(count)
    return answer