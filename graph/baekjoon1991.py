class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_node(self, parent: Node, *child ):
    if parent.left is None:
        parent.left = child[0]
    if parent.right is None:
        parent.right = child[1]


N = int(input())
nodes = []
for i in range(N):
    nodes.append(Node(chr(ord('A') + i)))

for i in range(N):
    n, l, r = input().split()
    curr = nodes[ord(n) - ord('A')]
    if l != '.':
        curr.left = nodes[ord(l) - ord('A')]
    if r != '.':
        curr.right = nodes[ord(r) - ord('A')]


def preorder_traversal(node: Node):
    if not node:
        return
    print(node.data, end='')
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node: Node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.data, end='')
    inorder_traversal(node.right)

def postorder_traversal(node: Node):
    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end='')

preorder_traversal(nodes[0])
print()
inorder_traversal(nodes[0])
print()
postorder_traversal(nodes[0])