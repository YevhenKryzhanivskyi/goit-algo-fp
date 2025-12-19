class MinHeap:
# Бінарна купа для зберігання пар (ключ, значення)

    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def insert(self, key, value):
        """Додає елемент у купу."""
        self.heap.append((key, value))
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Піднімає елемент вгору для збереження властивості купи.
        while index > 0 and self.heap[self.parent(index)][0] > self.heap[index][0]:
            self.heap[index], self.heap[self.parent(index)] = (
                self.heap[self.parent(index)],
                self.heap[index],
            )
            index = self.parent(index)

    def extract_min(self):
        # Видаляє і повертає мінімальний елемент з купи.
        if not self.heap:
            return None

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)

        return root

    def _heapify_down(self, index):
        # Опускає елемент вниз для збереження властивості купи.
        smallest = index
        left_child = self.left(index)
        right_child = self.right(index)

        if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def is_empty(self):
        """Перевіряє, чи купа порожня."""
        return len(self.heap) == 0


def dijkstra(graph, start):
   # Алгоритм Дейкстри для знаходження найкоротших шляхів від початкової вершини
    dist = {vertex: float('inf') for vertex in graph}
    dist[start] = 0

    heap = MinHeap()
    heap.insert(0, start)

    while not heap.is_empty():
        current_dist, current_vertex = heap.extract_min()

        if current_dist > dist[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            if dist[current_vertex] + weight < dist[neighbor]:
                dist[neighbor] = dist[current_vertex] + weight
                heap.insert(dist[neighbor], neighbor)

    return dist


# 🔹 Приклад використання
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }

    result = dijkstra(graph, 'A')
    print("Найкоротші відстані від вершини A:", result)