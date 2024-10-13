# Time: 1.30s	
# Mem: 24M

from typing import List, Tuple

class UnionFind:
    def __init__(self, num_nodes):
        self._parent = [-1] * num_nodes
        self._sizes = [1] * num_nodes

    def union(self, node_1: int, node_2: int):
        root_1 = self.find(self.find(node_1))
        root_2 = self.find(self.find(node_2))
        if root_1 == root_2:
            return
        self._parent[root_1] = root_2 # root_2 is parent of root_1
        self._sizes[root_2] += self._sizes[root_1]

    def find(self, node: int) -> int:
        parent = -1
        while True:
            parent = self._parent[node]
            if parent == -1:
                return node
            node = parent     

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
    root_1 = network.find(person_1)
    root_2 = network.find(person_2)
    if root_1 == root_2:
        return
    if network.size(root_1) + network.size(root_2)  <= limit_size:
        network.union(root_1, root_2)

def examine(network: UnionFind, person_1: int, person_2: int) -> bool:
    return "Yes" if (network.find(person_1) == network.find(person_2)) else "No"

def size(network: UnionFind, person: int) -> int:
    return network.size(person)