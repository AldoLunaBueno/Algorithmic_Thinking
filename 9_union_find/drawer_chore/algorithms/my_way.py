from typing import List, Tuple

def solve(n: int, d: int, pairs: List[Tuple]):
    chest = Chest(d+1)
    for drawer_1, drawer_2 in pairs:
        result = "LADICA" if chest.put_item_in(drawer_1, drawer_2) else "SMECE"
        print(result)
   
class Chest:
    def __init__(self, num_drawers: int):        
        self._dsu = UnionFind(num_drawers)
        self._items = [0] * num_drawers
    
    def put_item_in(self, drawer_1, drawer_2) -> bool:
        group_1 = self._dsu.find(drawer_1)
        group_2 = self._dsu.find(drawer_2)
        if group_1 == group_2:
            group = group_1
            num_drawers = self._dsu.size(group)
            num_items = self._items[group]
            if num_drawers > num_items:
                self._items[group] += 1
                return True
            else:
                return False
        num_drawers_1 = self._dsu.size(group_1)
        num_drawers_2 = self._dsu.size(group_2)
        num_items_1 = self._items[group_1]
        num_items_2 = self._items[group_2]
        if num_drawers_1 + num_drawers_2 > num_items_1 + num_items_2:
            group = self._dsu.union(group_1, group_2)
            self._items[group] += 1 + (self._items[group_1] if group != group_1 else self._items[group_2])
            return True
        else:
            return False
        

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