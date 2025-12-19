import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    # Ініціалізація вузла дерева

    def __init__(self, key, color="#CCCCCC"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    # Додає ребра до графа для візуалізації дерева
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


def draw_tree(tree_root, step_title=""):
    # Візуалізація дерева з використанням networkx і matplotlib
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

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
    plt.title(step_title)
    plt.show()


def generate_colors(n):
    # Генерує n кольорів від темно-синього до світло-блакитного
    colors = []
    for i in range(n):
        intensity = int(50 + (205 * i / (n - 1)))  
        hex_color = f"#{intensity:02x}{intensity:02x}f0"  
        colors.append(hex_color)
    return colors


def dfs(root):
    # Обхід у глибину (стек)
    stack = [root]
    visited = []
    colors = generate_colors(count_nodes(root))

    step = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            node.color = colors[len(visited)]
            visited.append(node)
            step += 1
            draw_tree(root, step_title=f"DFS крок {step}: відвідано {node.val}")
            # Додаємо правого і лівого (щоб лівий оброблявся першим)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def bfs(root):
    # Обхід у ширину (черга)
    queue = deque([root])
    visited = []
    colors = generate_colors(count_nodes(root))

    step = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            node.color = colors[len(visited)]
            visited.append(node)
            step += 1
            draw_tree(root, step_title=f"BFS крок {step}: відвідано {node.val}")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def count_nodes(root):
    # Підрахунок кількості вузлів у дереві
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            count += 1
            stack.append(node.left)
            stack.append(node.right)
    return count


if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Візуалізація обходів
    print("DFS:")
    dfs(root)

    # Скидаємо кольори перед BFS
    root.color = "#CCCCCC"
    root.left.color = "#CCCCCC"
    root.left.left.color = "#CCCCCC"
    root.left.right.color = "#CCCCCC"
    root.right.color = "#CCCCCC"
    root.right.left.color = "#CCCCCC"

    print("BFS:")
    bfs(root)