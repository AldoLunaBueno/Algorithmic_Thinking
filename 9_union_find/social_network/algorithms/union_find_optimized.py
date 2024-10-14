# Time: 1.18	
# Mem: 24M

from typing import List, Tuple

class UnionFind:
    """
    Implementation of the union-find operations based on disjoint set union (DSU) data structure
    """
    def __init__(self, num_nodes):
        self._parent = [-1] * num_nodes
        self._sizes = [1] * num_nodes

    def union(self, node_1: int, node_2: int):
        root_1 = self.find(node_1)
        root_2 = self.find(node_2)
        if root_1 == root_2:
            return
        # union by size
        if self.size(root_1) < self.size(root_2):
            root_1, root_2 = root_2, root_1 # root_1 subset is bigger 
        self._parent[root_2] = root_1 # root_1 is parent of root_2
        self._sizes[root_1] += self._sizes[root_2]

    def find(self, node: int) -> int:
        start_node = node
        while self._parent[node] != -1:
            node = self._parent[node]
        if start_node != node:
            self._parent[start_node] = node # path compression
        return node

    def size(self, node: int) -> int:
        root = self.find(node)
        return self._sizes[root]

def solve(n: int, m: int, q: List[Tuple]):
    network = UnionFind(n+1)
    for command, *args in q:
        if command == "A":
            add(network, *args, m)
        elif command == "E":
            print(examine(network, *args))
        elif command == "S":
            print(size(network, *args))

def add(network: UnionFind, person_1: int, person_2: int, limit_size: int):
    community_1 = network.find(person_1)
    community_2 = network.find(person_2)
    if community_1 == community_2:
        return
    if network.size(community_1) + network.size(community_2)  <= limit_size:
        network.union(community_1, community_2)

def examine(network: UnionFind, person_1: int, person_2: int) -> bool:
    return "Yes" if (network.find(person_1) == network.find(person_2)) else "No"

def size(network: UnionFind, person: int) -> int:
    return network.size(person)