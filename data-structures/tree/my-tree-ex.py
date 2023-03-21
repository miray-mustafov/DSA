class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


my_binary_tree = Node("Pet")

my_binary_tree.left_child = Node('Cat')
my_binary_tree.right_child = Node('Dog')

my_binary_tree.left_child.left_child = Node('Egyptian cat')
my_binary_tree.left_child.right_child = Node('Persian cat')

my_binary_tree.right_child.left_child = Node('Chau Chau')
my_binary_tree.right_child.right_child = Node('Pekines')

def preorder_traversal(tree_node):
    if not tree_node:
        return
    print(tree_node.data)
    preorder_traversal(tree_node.left_child)
    preorder_traversal(tree_node.right_child)

def inorder_traversal(tree_node):
    if tree_node.left_child:
        inorder_traversal(tree_node.left_child)
        inorder_traversal(tree_node.right_child)
        print(tree_node.left_child.data)
        print(tree_node.right_child.data)



print("Preorder traversal:")
preorder_traversal(my_binary_tree)

print("\nInorder traversal:")
inorder_traversal(my_binary_tree)




