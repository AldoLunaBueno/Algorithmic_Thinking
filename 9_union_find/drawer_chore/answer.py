# Drawer Chore (Ladice)
# DMOJ problem coci13c5p6

# Resources: 2.217s, 21.00 MB
# Maximum single-case runtime: 0.659s
# Final score: 7/7 (17.0/17 points)

from typing import List      
from sys import stdin
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
            return root_1
        # union by size
        if self.size(root_1) < self.size(root_2):
            root_1, root_2 = root_2, root_1 # root_1 subset is bigger 
        self._parent[root_2] = root_1 # root_1 is parent of root_2
        self._sizes[root_1] += self._sizes[root_2]
        return root_1 # return final representative

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

def put_item_in(dsu: UnionFind, items: List, drawer_1, drawer_2) -> bool:
    group_1 = dsu.find(drawer_1)
    group_2 = dsu.find(drawer_2)
    if group_1 == group_2:
        group = group_1
        num_drawers = dsu.size(group)
        num_items = items[group]
        if num_drawers > num_items:
            items[group] += 1
            return True
        else:
            return False
    num_drawers_1 = dsu.size(group_1)
    num_drawers_2 = dsu.size(group_2)
    num_items_1 = items[group_1]
    num_items_2 = items[group_2]
    if num_drawers_1 + num_drawers_2 > num_items_1 + num_items_2:
        group = dsu.union(group_1, group_2)
        items[group] += 1 + (items[group_1] if group != group_1 else items[group_2])
        return True
    else:
        return False

def main():
    num_items, num_drawers = [int(x) for x in stdin.readline().split(" ")]
    dsu = UnionFind(num_drawers+1)
    items = [0] * (num_drawers+1)
    for _ in range(num_items):
        d1, d2 = [int(x) for x in stdin.readline().split(" ")]
        result = "LADICA" if put_item_in(dsu, items, d1, d2) else "SMECE"
        print(result)

if __name__ == "__main__":
    main()