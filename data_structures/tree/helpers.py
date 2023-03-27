from graphviz import Digraph


def vertical_view(root_node):
    if not root_node:
        return print("tree empty")
    dot = Digraph()

    # helper function to draw each node and its children
    def draw_node(node):
        if not node:
            return
        dot.node(str(node.data))
        if node.left:
            dot.edge(str(node.data), str(node.left.data))
            draw_node(node.left)
        if node.right:
            dot.edge(str(node.data), str(node.right.data))
            draw_node(node.right)

    draw_node(root_node)
    dot.render(view=True)
