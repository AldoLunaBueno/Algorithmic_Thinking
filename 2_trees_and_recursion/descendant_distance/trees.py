from typing import List, Dict, Set

class Node:
    def __init__(self, name: str, children: List["Node"] = None) -> None:
        self.name = name
        if children == None:
            children = []
        self.children = children
        self.score = 0
    
    def insert_child(self, child: "Node"):
        self.children.append(child)

    def isleaf(self):
        return len(self.children) == 0

    def numb_nodes(self):
        if self.children == None:
            return 1
        result = 0
        for child in self.children:
            result += child.numb_nodes()
        return 1 + result
        
    def preorder(self) -> List["Node"]:
        result = [self]
        for child in self.children:
            result += child.preorder()
        return result
    
    def __str__(self, level = 0):
        result = "  " * level + self.name + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result
        
    

text = """A 2 B C	
B 2 D E
C 1 F
E 2 G H
F 2 I J
H 2 K L"""

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

def score_one(tree: Node, distance: int, level: int = 0) -> int:
    if level == distance:
        return 1
    result = 0
    for node in tree.children:
        result += score_one(node, distance, level + 1)
    return result



family_tree = text_to_tree(text)
print(family_tree)
nodes = family_tree.preorder()

for node in nodes:
    node.score = score_one(node, 2)

nodes = sorted(nodes, key = lambda node: node.name)
nodes = sorted(nodes, key = lambda node: node.score, reverse=True)

for node in nodes:
    print(node.name, node.score)
