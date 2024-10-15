from typing import List, Tuple

def solve(num_people: int, operations: List[Tuple]):
    war = War(num_people)
    for op, x, y in operations:
        if op == 1:
            result = war.set_friends(x, y)
        elif op == 2:
            result = war.set_enemies(x, y)
        elif op == 3:
            result = war.are_friends(x, y)
        elif op == 4:
            result = war.are_enemies(x, y)
        if result is not None:
            print(result)

class War:
    def __init__(self, num_people: int):
        self._dsu = UnionFind(num_people)
        self._enemy_of = [-1] * num_people # unknown enemies are -1

    def set_friends(self, person_1, person_2):        
        country_1 = self._dsu.find(person_1)
        country_2 = self._dsu.find(person_2)
        # enemies
        enemy_1 = self._enemy_of[country_1]
        enemy_2 = self._enemy_of[country_2]
        # are they enemies?
        if enemy_1 == country_2 or enemy_2 == country_1:
            return -1
        country = self._dsu.union(country_1, country_2)
        if enemy_1 == -1 and enemy_2 == -1:
            return
        elif enemy_1 != -1 and enemy_2 != -1:
            # can't be equal
            enemy = self._dsu.union(enemy_1, enemy_2)
            self._enemy_of[country] = enemy
            self._enemy_of[enemy] = country
        else:
            enemy = enemy_1 if enemy_1 != -1 else enemy_2
            self._enemy_of[country] = enemy
            self._enemy_of[enemy] = country

    def set_enemies(self, person_1, person_2):
        country_1 = self._dsu.find(person_1)
        country_2 = self._dsu.find(person_2)

        # are they friends?
        if country_1 == country_2:
            return -1
        
        # do they already have an enemy?
        enemy_1 = self._enemy_of[country_1]
        enemy_2 = self._enemy_of[country_2]
        
        if enemy_1 == -1 and enemy_2 == -1:
            pass
        elif enemy_1 != -1 and enemy_2 != -1:
            country_1 = self._dsu.union(country_1, enemy_2)
            country_2 = self._dsu.union(country_2, enemy_1)
        else:
            if enemy_1 != -1:
                country_2 = self._dsu.union(country_2, enemy_1)
            elif enemy_2 != -1:
                country_1 = self._dsu.union(country_1, enemy_2)
        
        # making enemies of the resulting groups
        self._enemy_of[country_2] = country_1
        self._enemy_of[country_1] = country_2

    def are_friends(self, person_1, person_2):
        country_1 = self._dsu.find(person_1)
        country_2 = self._dsu.find(person_2)
        return 1 if country_1 == country_2 else 0

    def are_enemies(self, person_1, person_2):
        country_1 = self._dsu.find(person_1)
        country_2 = self._dsu.find(person_2)
        return 1 if self._enemy_of[country_1] == country_2 else 0

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