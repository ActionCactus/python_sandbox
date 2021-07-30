from src.linked_list.linked_list import Node, DLNode, LinkedList
import pytest


def test_empty_list_has_len_0():
    assert len(LinkedList()) == 0


def test_len_of_one_with_added_items():
    assert len(LinkedList(Node(0))) == 1


def test_appending_node():
    node_a = Node(0)
    ll = LinkedList(node_a)
    ll.append(Node(1))

    assert len(ll) == 2
    assert node_a.next.value == 1


def test_appending_dlnode():
    node_a = DLNode(0)
    node_b = DLNode(1)
    ll = LinkedList(node_a)
    ll.append(node_b)

    assert len(ll) == 2
    assert node_a.next.value == 1
    assert node_a.last is None
    assert node_b.last.value == 0
    assert node_b.next is None


def test_appending_to_empty_ll():
    ll = LinkedList()
    ll.append(Node(0))

    assert len(ll) == 1
    assert ll.head.value == 0


def test_inserting_into_empty_ll():
    ll = LinkedList()
    ll.insert(Node(0), 0)

    assert len(ll) == 1


def test_inserting_into_empty_ll_at_invalid_position():
    with pytest.raises(ValueError):
        LinkedList().insert(Node(0), 100)


def test_inserting_at_invalid_position():
    ll = LinkedList(Node(0))

    with pytest.raises(ValueError):
        ll.insert(Node(1), 100)


def test_inserting_into_front():
    ll = LinkedList(Node(0))
    ll.insert(Node(1), 0)
    assert len(ll) == 2
    assert ll.head.value == 1


def test_inserting_into_middle():
    ll = LinkedList(Node(0))
    ll.append(Node(1))
    ll.insert(Node(2), 1)

    assert len(ll) == 3
    assert ll.head.value == 0
    assert ll.tail.value == 1
    assert ll.head.next.value == 2


def test_inserting_into_back():
    ll = LinkedList(Node(0))
    ll.insert(Node(1), 1)
    assert len(ll) == 2
    assert ll.tail.value == 1
