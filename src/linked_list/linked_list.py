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
            self.tail = node

    def insert(self, node: Node, position: int):
        focus = self.head

        if position == 0:
            self._update_nodes(node, focus, None)
            self.head = node
            return

        idx = 0
        while focus:
            if position == idx + 1:
                # Doing this here instead of the next iteration because singly linked lists won't have
                # a ref to 'last' to update
                if not focus.next:
                    self.tail = node
                self._update_nodes(node, focus.next, focus)
                break
            idx += 1
            focus = focus.next

        if (idx + 1) < position:
            raise ValueError(
                f"Can't add node to position {position} - list is only length {idx}!"
            )

    def prepend(self, node: Node):
        self._update_nodes(node, self.head, None)
        self.head = node

    def delete(self, position: int):
        focus = self.head

        idx = 0
        deleted = False
        last = None
        while focus and not deleted:
            if position == idx:
                # Delete focus
                deleted = True
                if not last:
                    # Delete the head
                    if focus.next:
                        self._update_nodes(focus.next, focus.next.next, None)
                        self.head = focus.next
                        break
                    else:
                        self.head = None
                        self.tail = None
                        break
                else:
                    if focus.next:
                        self._update_nodes(focus.next, focus.next.next, last)
                        break
                    else:
                        self._update_nodes(
                            last,
                            None,
                            last.last if isinstance(last, DLNode) else None
                        )
                        self.tail = last
                        break

            idx += 1
            last = focus
            focus = focus.next

        if not deleted:
            raise ValueError(f"No node exists at position {position}!")

    def remove_duplicates(self):
        # assume all values hashable for now.  Check isinstance(x, collections.Hashable) if needed
        cache = {}
        focus = self.head
        last = None
        while focus:
            if focus.value not in cache:
                # No duplicate found - remember this value
                cache[focus.value] = 0
                last = focus
                focus = focus.next
            else:
                if not focus.next:
                    # trim the tail
                    last.next = None
                    self.tail = last
                    break
                focus = focus.next
                self._update_nodes(focus, focus.next, last)
                last = focus
                focus = focus.next

    def __len__(self):
        length = 0

        focus = self.head
        while focus:
            length += 1
            focus = focus.next

        return length

    def _update_nodes(self, node: Node, next: Node, last: Node):
        if not node:
            return

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


def is_palindrome(ll: LinkedList) -> bool:
    if ll.assigned_type == DLNode:
        # for doubly linked lists we can converge and therefore do this in one iteration
        left_ref = ll.head
        right_ref = ll.tail
        while left_ref.next:
            if left_ref.value != right_ref.value:
                return False

            left_ref = left_ref.next
            right_ref = right_ref.last
        return True
    else:
        vals = []
        focus = ll.head
        while focus:
            vals.append(focus.value)
            focus = focus.next

        idx = 0
        while idx < (len(vals) / 2):
            x = vals[-idx]
            y = vals[idx]
            if vals[idx] != vals[-(idx + 1)]:
                return False
            idx += 1

        return True
