graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 3)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 2,
    'D': 1,
    'G': 0
}


def a_star(start, goal):
    open_list = [(start, 0)]
    closed_list = []

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        open_list.sort(key=lambda x: g_cost[x[0]] + heuristic[x[0]])

        current = open_list.pop(0)[0]

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        closed_list.append(current)

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                open_list.append((neighbor, new_g))

    return None


path = a_star('S', 'G')
print("Shortest Path:", path)
