from typing import List, Tuple

class Node:
    def __init__(self, value: int = 0, left: "Node" = None, right: "Node" = None) -> None:
        self.value = value
        self.right = right
        self.left =  left
    def isleaf(self: "Node"):
        return self.left == self.right == None
    def tree_sum_by_recursion(self: "Node"):
        if self.isleaf():
            return self.value
        left = self.left.tree_sum_by_recursion()
        right = self.right.tree_sum_by_recursion()
        return left + right
    def numb_nodes(self: "Node"):
        if self.isleaf():
            return 1
        return 1 + self.left.numb_nodes() + self.right.numb_nodes()
    def numb_leafs(self: "Node"):
        if self.isleaf():
            return 1
        return self.left.numb_leafs() + self.right.numb_leafs()
    def numb_edges(self: "Node"):
        if self.isleaf():
            return 0
        return 2 + self.left.numb_edges() + self.right.numb_edges()
    def depth(self: "Node"):
        if self.isleaf():
            return 0
        return 1 + max(self.left.depth(), self.right.depth())

def tree_sum_by_iteration(root: Node):
    result = 0 # value accumulator
    stack: List[Node] = [None]
    curr_node: Node = root
    while curr_node != None: # end of stack
        if not curr_node.isleaf():
            stack.append(curr_node.left) # store pending subtree
            curr_node = curr_node.right # next subtree to process
            continue
        result += curr_node.value
        curr_node = stack.pop() # next subtree to process
    return result

four = Node(4)
nine = Node(9)
b = Node(left=four, right=nine)
fifteen = Node(15)
c = Node(left=b, right=fifteen)

print("Tree functions:")
print(c.tree_sum_by_recursion())
print(c.numb_nodes())
print(c.numb_leafs())
print(c.numb_edges())
print(c.depth())

def text_to_tree(s: str, i: int = 0) -> Tuple[Node, int]:
    value = ""
    while s[i].isnumeric():
        value += s[i]
        i += 1
    if value != "":
        return Node(int(value)), i
    
    left, i = text_to_tree(s, i+1)
    right, i = text_to_tree(s, i+1)

    return Node(left=left, right=right), i+1

tree_string = "(((10 10) (10 10)) (10 10))\n"
ten, _ = text_to_tree(tree_string)

print("Text to Tree:")
print(ten.tree_sum_by_recursion())