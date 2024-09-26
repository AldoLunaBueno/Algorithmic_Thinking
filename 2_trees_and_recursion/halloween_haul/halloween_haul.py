# Halloween Haul (Trick or Tree'ing)
# DMOJ problem dwite12c1p4

# Resources: 0.031s, 11.44 MB
# Maximum single-case runtime: 0.031s
# Final score: 10/10 (5.0/5 points)

from typing import List, Tuple

def main():
    trees = get_data()
    solve(trees)

def get_data():
    trees: List[Node] = []
    while True:
        tree_string = ""
        try:
            tree_string = input()+"\n"
        except EOFError:
            break
        tree = text_to_tree(tree_string)
        trees.append(tree)
    return trees


class Node:
    def __init__(self, value: int = 0, left: "Node" = None, right: "Node" = None) -> None:
        self.value = value
        self.right = right
        self.left =  left

    def isleaf(self: "Node") -> bool:
        return self.left == self.right == None
    
    def sum(self: "Node") -> int:
        if self.isleaf():
            return self.value
        left = self.left.sum()
        right = self.right.sum()
        return left + right
    
    def complete_traversal(self: "Node") -> int:
        if self.isleaf():
            return 0
        return 4 + self.left.complete_traversal() + self.right.complete_traversal()
    
    def depth(self: "Node") -> int:
        if self.isleaf():
            return 0
        return 1 + max(self.left.depth(), self.right.depth())

def text_to_tree(s: str) -> Node:
    root, _ = _text_to_tree(s, 0)
    return root

def _text_to_tree(s: str, i: int) -> Tuple[Node, int]:
    value = ""
    while s[i].isnumeric():
        value += s[i]
        i += 1
    if value != "":
        return Node(int(value)), i
    
    left, i = _text_to_tree(s, i+1)
    right, i = _text_to_tree(s, i+1)

    return Node(left=left, right=right), i+1

def solve(trees: List[Node]):
    for tree in trees:
        min_roads_to_traverse = tree.complete_traversal() - tree.depth()
        total_candy = tree.sum()
        print(min_roads_to_traverse, total_candy)

if __name__ == "__main__":
    main()