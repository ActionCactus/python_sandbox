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