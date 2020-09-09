class TreeNode:

    def __init__(self, name):
        self.name = name
        self.children = []

class BinaryTreeNode:

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def in_order(node, visit):
    if node != None:
        in_order(node.left, visit)
        visit(node)
        in_order(node.right, visit)

def pre_order(node, visit):
    if node != None:
        visit(node)
        pre_order(node.left, visit)
        pre_order(node.right, visit)

def pos_order(node, visit):
    if node != None:
        pos_order(node.left, visit)
        pos_order(node.right, visit)
        visit(node)

if __name__ == '__main__':
    root = BinaryTreeNode("0")
    n1 = BinaryTreeNode("1")
    n2 = BinaryTreeNode("2")
    n3 = BinaryTreeNode("3")
    n4 = BinaryTreeNode("4")

    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4

    in_order(root, lambda node: print(node.name))
    print("")
    pre_order(root, lambda node: print(node.name))
    print("")
    pos_order(root, lambda node: print(node.name))


