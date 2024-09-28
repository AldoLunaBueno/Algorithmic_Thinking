from typing import List, Dict, Set

import sys
sys.setrecursionlimit(1500)

# Resources: 0.114s, 13.40 MB
# Maximum single-case runtime: 0.114s
# Final score: 100/100 (10.0/10 points)

def main():
    trees, distances = get_data()
    solve(trees, distances)
    # tree = trees[0]
    # print(tree)
    # print(len(tree.preorder()))

class Node:
    def __init__(self, name: str, children: List["Node"] = None) -> None:
        self.name = name
        if children == None:
            children = []
        self.children = children
        self.score = 0
    
    def isleaf(self):
        return len(self.children) == 0
    
    def insert_child(self, child: "Node"):
        self.children.append(child)
    
    # Useful for debugging text_to_tree() at a glance
    def __str__(self, level = 0):
        result = "  " * level + self.name + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result
    
    def preorder(self) -> List["Node"]:
        result = [self]
        for child in self.children:
            result += child.preorder()
        return result
        
def text_to_tree(text: str) -> Node:
    lines = text.split("\n")
    name_to_node: Dict[str, Node] = {}
    all_fathers: Set[Node] = set()
    all_children: Set[Node] = set()
    for line in lines:
        father_name, _, *child_names = line.split(" ")
        father: Node = None
        if father_name not in name_to_node:
            name_to_node[father_name] = Node(father_name)
        father = name_to_node[father_name]
        for child_name in child_names:
            if child_name not in name_to_node:
                name_to_node[child_name] = Node(child_name)
            father.insert_child(name_to_node[child_name])
        all_fathers.add(father)
        all_children.update(set(father.children))
    root = all_fathers - all_children 
    return list(root)[0]

def get_data():
    trees: List[Node] = []
    distances: List[int] = []
    n = int(input())
    for _ in range(n):
        m, d = [int(x) for x in input().split(" ")]
        
        # My 1 hour error was due to relying on data cleanliness
        # The strip() safed the day
        text = [input().strip() for _ in range(m)]
        
        text = "\n".join(text)
        tree = text_to_tree(text)
        trees.append(tree)
        distances.append(d)
    return trees, distances

def solve(trees: List[Node], distances: List[int]):
    for index, (tree, distance) in enumerate(zip(trees, distances), 1):
        nodes = tree.preorder()
        selected_nodes: List[Node] = []
        for node in nodes:
            score = score_one(node, distance)
            if score != 0:
                node.score = score
                selected_nodes.append(node)
        nodes = selected_nodes

        # The next multisort works because the sort stability 
        # of the build-in sorted() method:

        # sort on secondary key
        nodes = sorted(nodes, key = lambda node: node.name)
        # sort on primary key
        nodes = sorted(nodes, key = lambda node: node.score, reverse=True)
        
        print(f"Tree {index}:")
        i = 0
        while i < len(nodes):
            if i >= 3 and nodes[i].score != nodes[i-1].score:
                break
            print(nodes[i].name, nodes[i].score)
            i += 1
        print()

def score_one(tree: Node, distance: int, level: int = 0) -> int:
    if level == distance:
        return 1
    result = 0
    for node in tree.children:
        result += score_one(node, distance, level + 1)
    return result

if __name__ == "__main__":
    main()