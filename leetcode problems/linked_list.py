class Node:
    def __init__(self, val=None, next_node=None):
        self.data = val
        self.next: Node = next_node


class Tracker:
    def __init__(self):
        self.head: Node = None

    def insert_node(self, node: Node):
        new_node = node
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        return self

    def print_all_nodes(self):
        i = 1
        while self.head:
            print(self.head.data)
            self.head = self.head.next


tracker = Tracker().insert_node(Node(3))
tracker.insert_node(Node(5))
tracker.insert_node(Node(7))
tracker.insert_node(Node(9))
tracker.print_all_nodes()
