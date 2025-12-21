class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return

        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next

        if cur is None:
            return

        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Реверсування списку."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        """Сортування списку методом bubble sort."""
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Об’єднання двох відсортованих списків."""
        dummy = Node(0)
        tail = dummy
        a, b = list1.head, list2.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_end(30)
    llist.insert_at_end(10)
    llist.insert_at_end(20)

    print("Початковий список:")
    llist.print_list()

    # Сортування
    llist.sort()
    print("\nВідсортований список:")
    llist.print_list()

    # Реверсування
    llist.reverse()
    print("\nРеверсований список:")
    llist.print_list()

    # Об’єднання двох відсортованих списків
    llist1 = LinkedList()
    llist1.insert_at_end(1)
    llist1.insert_at_end(3)
    llist1.insert_at_end(5)

    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(4)
    llist2.insert_at_end(6)

    merged = LinkedList.merge_sorted_lists(llist1, llist2)
    print("\nОб’єднаний відсортований список:")
    merged.print_list()
