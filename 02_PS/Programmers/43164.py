def solution(tickets):
    graph = {}

    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)

    for key in graph:
        graph[key].sort(reverse=True)

    route = []
    stack = ["ICN"]

    while stack:
        top = stack[-1]

        if top in graph and graph[top]:
            stack.append(graph[top].pop())
        else:
            route.append(stack.pop())

    return route[::-1]