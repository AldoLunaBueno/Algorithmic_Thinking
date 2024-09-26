from typing import List

class Node:
    def __init__(self, value: int = 0, left: "Node" = None, right: "Node" = None) -> None:
        self.value = value
        self.right = right
        self.left =  left
    def tree_sum_by_recursion(self: "Node"):
        if self.left == self.right == None:
            return self.value
        value_l = self.left.tree_sum_by_recursion()
        value_r = self.right.tree_sum_by_recursion()
        return value_l + value_r

def tree_sum_by_iteration(root: Node):
    result = 0 # value accumulator
    stack: List[Node] = [None]
    curr_node: Node = root
    while True:
        if curr_node.left == curr_node.right == None: # leaf
            result += curr_node.value
            curr_node = stack.pop() # next subtree to process
            if curr_node == None: # end of stack
                break
            continue
        stack.append(curr_node.left) # pending subtree
        curr_node = curr_node.right # next subtree to process
        
    return result

four = Node(4)
nine = Node(9)
b = Node(left=four, right=nine)
fifteen = Node(15)
c = Node(left=b, right=fifteen)

print(c.tree_sum_by_recursion())
print(tree_sum_by_iteration(c))
