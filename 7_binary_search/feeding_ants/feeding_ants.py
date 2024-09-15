# Feeding ants
# DMOJ coci14c4p4 problem

from typing import List, Dict, Tuple, Callable

EdgeDict = Dict[int, List[Tuple[int]]]
MAX_LITERS = 2_000_000_000

def main():
    E, V = get_data()
    solve(E, V)

def get_data() -> Tuple[EdgeDict, List[int]]:
    """
    Gets data and returns it like an adjacency list of edges 
    plus a list of node values.
    """
    n = int(input())
    edges: EdgeDict = {}
    edges = { i:[] for i in range(1, n+1) }
    for _ in range(n-1):
        edge = input().split(" ")
        node, to_node, percent, is_super = [int(x) for x in edge]
        edges[node].append((to_node, percent, is_super))
    node_values = [-1] + [int(x) for x in input().split(" ")]
    return edges, node_values

def solve(edges: EdgeDict, node_values: List[int]):
    edges[0] = [(1, 100, 0)] # special node to begin the DFS
    f = lambda liters: 1 if can_fed(liters, edges, node_values) else -1
    liters = bisection_method(f, 0, MAX_LITERS)
    print(liters)


def can_fed(liters: float, edges: EdgeDict, liters_needed_list: int, node: int = 0):
    """
    Returns True or False depending on whether all ants are fed or no  
    given some liters of water from the given node downwards the tree.
    """
    for edge in edges[node]:
        to_node, percent, is_super = edge
        curr_liters = liters * percent / 100
        if is_super and curr_liters > 1:
            # curr_liters **= 2 # Overflow
            curr_liters *= curr_liters
        ant_needs = liters_needed_list[to_node]
        if ant_needs != -1 and ant_needs > curr_liters:
            return False # leaf fail
        if not can_fed(curr_liters, edges, liters_needed_list, to_node):
            return False # downwars tree fail
    
    return True

def bisection_method(f: Callable, low: float, high: float, abs_tol = 0.001):
    diff = high - low
    while diff > abs_tol:
        c = low + (high-low)/2
        if f(c) < 0:
            low = c
        elif f(c) > 0:
            high = c
        elif f(c) == 0:
            return c
        diff = high - low
    return high

        


if __name__ == "__main__":
    main()