from typing import List, Dict

class Node:
    def __init__(self, name: str, children: List["Node"] = None) -> None:
        self.name = name
        if children == None:
            children = []
        self.children = children
    
    def insert_child(self, child: "Node"):
        self.children.append(child)

    def numb_nodes(self):
        if self.children == None:
            return 1
        result = 0
        for child in self.children:
            result += child.numb_nodes()
        return 1 + result
    
    def __str__(self, level = 0):
        result = "  " * level + self.name + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result
        
    

text = """Lucas 1 Enzo
Sana 2 Gabriel Lucas
Enzo 2 Min Becky
Kevin 2 Jad Cassie
Amber 4 Vlad Sana Ashley Kevin
Zara 1 Amber
Vlad 1 Omar"""

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

family_tree = text_to_tree(text)
print(family_tree)