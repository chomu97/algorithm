import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 아래 함수는 O(nlogn)
def add_node(parent: Node, key: int):
    if parent is None:
        return Node(key)
    if parent.data > key:
        parent.left = add_node(parent.left, key)
        return parent
    else:
        parent.right = add_node(parent.right, key)
        return parent

#하지만 스택을 이용하여 구현하면 O(n)
def construct_tree(preorder):
    if not preorder:
        return None
    root = Node(preorder[0])
    stack = [root]

    for val in preorder[1:]:
        node = Node(val)

        if val < stack[-1].data:
            stack[-1].left = node
        else:
            while stack and val > stack[-1].data:
                last_pop = stack.pop()
            last_pop.right = node
        stack.append(node)
    return root



def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data)

n, *file = open(0)
# root = Node(int(n))
# for i in file:
    # add_node(root, int(i.rstrip())) # nlogn 걸리는 로직.
preorder = [int(n)] + list(map(int, file))
root = construct_tree(preorder)
postorder_traversal(root)