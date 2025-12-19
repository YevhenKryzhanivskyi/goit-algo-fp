import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    # Ініціалізація вузла дерева

    def __init__(self, key, color="green"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # унікальний ID для кожного вузла


def build_heap_tree(heap, i=0):
    # Рекурсивне побудова дерева з купи
    if i >= len(heap):
        return None
    node = Node(heap[i])
    node.left = build_heap_tree(heap, 2 * i + 1)
    node.right = build_heap_tree(heap, 2 * i + 2)
    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Додає вузли та ребра у граф для візуалізації.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap):
    # Візуалізує купу як дерево
    root = build_heap_tree(heap)
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


if __name__ == "__main__":
    # Приклад використання
    heap = [10, 7, 9, 5, 6, 8]
    draw_heap(heap)