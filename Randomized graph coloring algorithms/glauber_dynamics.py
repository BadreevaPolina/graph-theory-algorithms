import random


def update(graph, coloring, k):
    u = random.choice(graph['V'])
    c = random.randint(1, k)
    if all(coloring[v] != c for v in graph['V'] if (u, v) in graph['E'] or (v, u) in graph['E']):
        coloring[u] = c


def glauber_dynamics(graph, k, t):
    coloring = {v: random.randint(1, k) for v in graph['V']}
    for _ in range(t):
        update(graph, coloring, k)
    return coloring