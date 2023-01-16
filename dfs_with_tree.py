class Node:
    def __init__(self,value, left= None, right= None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return "Node ("+ str(self.value)+")"

# 1st method / recursive
def walk_preorder(tree):
    print("up")
    if tree is not None:
        print(tree)
        walk_preorder(tree.left)
        walk_preorder(tree.right)

def walk_inorder(tree):
    print("up")
    if tree is not None:
        walk_inorder(tree.left)
        print(tree)
        walk_inorder(tree.right)

def walk_postorder(tree):
    print("up")
    if tree is not None:
        walk_postorder(tree.left)
        walk_postorder(tree.right)
        print(tree)

# 2nd method / iterative
def walk2(tree,stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)

mytree = Node('A', Node('B', Node('D'), Node('E')) , Node('C', Node('F'), Node('G')))

print("pre order")
walk_preorder(mytree)
print("in order")
walk_inorder(mytree)
print("post order")
walk_postorder(mytree)

print("iterative")
walk2(mytree, [])

