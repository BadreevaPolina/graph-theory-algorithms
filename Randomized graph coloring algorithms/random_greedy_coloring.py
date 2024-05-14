import random


def greedy_coloring(graph):
    coloring = {}
    for v in graph['V']:
        for k in range(1, len(graph['V']) + 1):
            if all(coloring.get(neighbour) != k for neighbour in graph['E'] if v in neighbour):
                coloring[v] = k
                break
    return coloring


def random_coloring(graph, iterations):
    best_coloring = None
    best_color_count = float('inf')

    for _ in range(iterations):
        vertices = graph['V']
        random.shuffle(vertices)
        current_coloring = greedy_coloring({'V': vertices, 'E': graph['E']})
        current_color_count = max(current_coloring.values())

        if current_color_count < best_color_count:
            best_coloring = current_coloring
            best_color_count = current_color_count

    return best_coloring
