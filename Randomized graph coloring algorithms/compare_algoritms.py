import time
import tracemalloc

from glauber_dynamics import glauber_dynamics
from vertex_descent import vertex_descent

examples = [
    {
        'V': ['A', 'B', 'C', 'D'],
        'E': [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C')]
    },
    {
        'V': ['A', 'B', 'C', 'D', 'E'],
        'E': [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')]
    },
{
    'V': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'E': [
        ('A', 'B'), ('A', 'C'), ('A', 'D'),
        ('B', 'C'), ('B', 'E'),
        ('C', 'D'), ('C', 'F'),
        ('D', 'G'),
        ('E', 'F'), ('E', 'H'),
        ('F', 'G'), ('F', 'H'),
        ('G', 'H')
    ]
}
]

t = 5000
k = 4
for graph in examples:
    tracemalloc.start()

    start_time = time.time()
    glauber_dynamics_res = glauber_dynamics(graph, k, t)
    elapsed_time_glauber_dynamics = time.time() - start_time

    current_glauber_dynamics, peak_glauber_dynamics = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tracemalloc.start()

    start_time = time.time()
    vertex_descent_res = vertex_descent(graph, k)
    elapsed_time_vertex_descent = time.time() - start_time

    current_vertex_descent, peak_vertex_descent = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tracemalloc.start()

    start_time = time.time()
    random_greedy_coloring = vertex_descent(graph, t)
    elapsed_time_random_greedy_coloring = time.time() - start_time

    current_random_greedy_coloring, peak_random_greedy_coloring = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"glauber_dynamics: {glauber_dynamics_res}")
    print(f"vertex_descent: {vertex_descent_res}")
    print(f"vertex_descent: {random_greedy_coloring}")
    print(f"Время выполнения: glauber_dynamics = {elapsed_time_glauber_dynamics:.4f} "
          f"vs  vertex_descent = {elapsed_time_vertex_descent:.4f} "
          f"vs random_greedy_coloring = {elapsed_time_random_greedy_coloring:.4f}")
    print(f"Использовано памяти: glauber_dynamics = {current_glauber_dynamics / 10**6:.4f} MB "
          f"vs vertex_descent = {current_vertex_descent / 10 ** 6:.4f} MB "
          f"vs random_greedy_coloring = {current_random_greedy_coloring / 10 ** 6:.4f} MB")
    print()
