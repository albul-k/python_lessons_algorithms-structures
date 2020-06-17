'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
'''


def dijkstra(graph: list, start: int):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [None for _ in range(len(graph))]

    _t = []

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):

            if not vertex == 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):

            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                _t.append(i)

    return cost, _t


if __name__ == "__main__":
    g = [
        [0, 0, 1, 1, 9, 0, 0, 0],
        [0, 0, 9, 4, 0, 0, 5, 0],
        [0, 9, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 0]
    ]
    s = int(input('От какой вершины идти: '))
    print(dijkstra(g, s))
