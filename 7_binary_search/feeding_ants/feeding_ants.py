# Feeding ants
# DMOJ coci14c4p4 problem

from typing import List, Dict, Tuple

EdgeDict = Dict[int, List[int]]

def main():
    E, V = get_data()
    solve(E, V)

def get_data() -> Tuple[EdgeDict, List[int]]:
    """
    Get data and return it like an adjacency list of edges 
    plus a list of node values.
    """
    n = int(input())
    edges: EdgeDict = {}
    edges = { i:[] for i in range(1, n+1) }
    for _ in range(n-1):
        edge = input().split(" ")
        father, son, percent, is_super = [int(x) for x in edge]
        edges[father].append((son, percent, is_super))
    node_values = [None] + [int(x) for x in input().split(" ")]
    return edges, node_values

def solve(edges: EdgeDict, node_values: List[int]):
    pass

if __name__ == "__main__":
    main()