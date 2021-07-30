class Node:
    def __init__(self, value, next: "Node" = None):
        self.next = next
        self.value = value


class DLNode(Node):
    def __init__(self, value, next: "DLNode" = None, last: "DLNode" = None):
        super().__init__(value, next)
        self.last = last


class LinkedList:
    def __init__(self, head: Node = None) -> None:
        self.head = head
        self.tail = head
        self.assigned_type = type(head) if head else None

    def append(self, node: Node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self._update_nodes(node, None, self.tail)

    def insert(self, node: Node, position: int):
        focus = self.head

        if not focus and position == 0:
            self.append(node)
            return

        idx = 0
        while focus:
            if idx == position:
                self._update_nodes(node, focus.next, focus)
                if idx == 0:
                    self.head = node
                elif focus.next is None:
                    self.tail = node
                break
            idx += 1
            focus = focus.next

        if idx < position:
            raise ValueError(
                f"Can't add node to position {position} - list is only length {idx}!"
            )

    def prepend(self, node: Node):
        pass

    def delete(self, position: int):
        pass

    def pop(self):
        pass

    def __len__(self):
        length = 0

        focus = self.head
        while focus:
            length += 1
            focus = focus.next

        return length

    def _update_nodes(self, node: Node, next: Node, last: Node):
        if not self.assigned_type:
            self.assigned_type = type(node)

        if self.assigned_type == Node:
            node.next = next
        elif self.assigned_type == DLNode:
            node.next = next
            node.last = last

            if next:
                next.last = node

        if last:
            last.next = node
