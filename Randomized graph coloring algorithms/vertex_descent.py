import random

def calculate_conflicts(graph, coloring):
    return sum(1 for (v, w) in graph['E'] if coloring[v] == coloring[w])


def vertex_descent(graph, k):
    V, E = graph['V'], graph['E']
    coloring = {v: random.randint(1, k) for v in V}
    Sbest = coloring.copy()
    fbest = calculate_conflicts(graph, Sbest)

    while True:
        conflicts = [v for v in V if any(coloring[v] == coloring[w] for w in V if (v, w) in E or (w, v) in E)]
        if not conflicts:
            break

        best_move = None
        best_conflicts = float('inf')
        for v in conflicts:
            for c in range(1, k + 1):
                if c != coloring[v]:
                    old_color = coloring[v]
                    coloring[v] = c
                    current_conflicts = calculate_conflicts(graph, coloring)
                    if current_conflicts < best_conflicts:
                        best_move = (v, c)
                        best_conflicts = current_conflicts
                    coloring[v] = old_color

        if best_move:
            v, c = best_move
            coloring[v] = c

        if fbest > best_conflicts:
            fbest = best_conflicts
            Sbest = coloring.copy()

    return Sbest