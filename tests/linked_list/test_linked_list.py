from src.linked_list.linked_list import Node, DLNode, LinkedList, is_palindrome
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


def test_prepending_empty_ll():
    ll = LinkedList()
    ll.prepend(Node(0))
    assert len(ll) == 1
    assert ll.head.value == 0


def test_prepending_ll():
    ll = LinkedList(Node(0))
    ll.append(Node(1))
    ll.prepend(Node(2))

    assert len(ll) == 3
    assert ll.head.value == 2
    assert ll.tail.value == 1


def test_cant_delete_from_empty_ll():
    with pytest.raises(ValueError):
        LinkedList().delete(0)


def test_cant_delete_position_out_of_range_which_isnt_head():
    ll = LinkedList(Node(0))
    ll.append(Node(1))
    with pytest.raises(ValueError):
        ll.delete(50)


def test_deleting_head():
    ll = LinkedList(Node(0))
    ll.delete(0)

    assert len(ll) == 0
    assert ll.head == None
    assert ll.tail == None


def test_deleting_head_of_elongated_ll():
    ll = LinkedList(Node(0))
    ll.append(Node(1))
    ll.delete(0)

    assert len(ll) == 1
    assert ll.head.value == 1
    assert ll.tail.value == 1


def test_deleting_tail():
    ll = LinkedList(Node(0))
    ll.append(Node(1))
    ll.delete(1)

    assert len(ll) == 1
    assert ll.head.value == 0
    assert ll.tail.value == 0


def test_deleting_item_in_middle():
    ll = LinkedList(Node(0))
    ll.append(Node(1))
    ll.append(Node(2))

    ll.delete(1)

    assert len(ll) == 2
    assert ll.head.value == 0
    assert ll.tail.value == 2


def test_inserting_dlnodes_to_middle_of_ll_updates_last_values():
    ll = LinkedList(DLNode(0))
    ll.append(DLNode(1))
    ll.insert(DLNode(2), 1)

    assert len(ll) == 3
    assert ll.head.value == 0
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 1


def test_removing_duplicates_on_empty_ll_results_in_no_errors():
    ll = LinkedList()
    ll.remove_duplicates()


def test_removing_duplicates_when_there_are_none_results_in_no_changes():
    ll = LinkedList(Node(1))
    ll.append(Node(2))
    ll.append(Node(3))
    ll.remove_duplicates()
    assert len(ll) == 3
    assert ll.head.value == 1
    assert ll.tail.value == 3


def test_removing_duplicates_with_hashable_values():
    ll = LinkedList(Node(1))
    ll.append(Node(2))
    ll.append(Node(1))
    assert len(ll) == 3
    ll.remove_duplicates()
    assert len(ll) == 2
    assert ll.tail.value == 2


def test_removing_duplicate_hashable_values_with_dupe_in_middle_of_ll():
    ll = LinkedList(Node(1))
    ll.append(Node(1))
    ll.append(Node(2))
    ll.remove_duplicates()
    assert len(ll) == 2
    assert ll.head.value == 1
    assert ll.tail.value == 2


def test_is_palindrome():
    build_palindrome(Node)
    global seeded_ll
    assert is_palindrome(seeded_ll) is True


def test_is_not_palindrome():
    ll = LinkedList(Node(1))
    ll.append(Node(2))
    ll.append(Node(3))
    ll.append(Node(1))
    assert is_palindrome(ll) is False


def test_odd_length_palindrome():
    build_palindrome(Node, True)
    global seeded_ll
    assert is_palindrome(seeded_ll) is True


seeded_ll = None


def seed_base_ll():
    global seeded_ll
    seeded_ll = LinkedList()
    for _i in range(0, 100):
        seeded_ll.append(Node(None))


def prepend_nodes():
    global seeded_ll
    for _i in range(0, 10):
        seeded_ll.prepend(Node(None))


def append_nodes():
    global seeded_ll
    for _i in range(0, 10):
        seeded_ll.append(Node(None))


def insert_nodes():
    global seeded_ll
    for i in range(50, 60):
        seeded_ll.insert(Node(None), i)


def check_if_palindrome():
    global seeded_ll
    is_palindrome(seeded_ll)


def build_palindrome(node_type, odd=False):
    global seeded_ll
    seeded_ll = LinkedList()

    insertion_range = range(0, 100)
    for i in insertion_range:
        seeded_ll.append(node_type(i))

    if odd:
        seeded_ll.append(node_type(i + 1))

    for i in reversed(insertion_range):
        seeded_ll.append(node_type(i))


def build_dl_palindrome():
    build_palindrome(DLNode)


def build_sl_palindrome():
    build_palindrome(Node)


def test_benchmarking_prepend(benchmark):
    benchmark.pedantic(
        prepend_nodes,
        setup=seed_base_ll,
        iterations=1,
        rounds=100
    )


def test_benchmarking_append(benchmark):
    benchmark.pedantic(
        append_nodes,
        setup=seed_base_ll,
        iterations=1,
        rounds=100
    )


def test_benchmarking_middle_insertion(benchmark):
    benchmark.pedantic(
        insert_nodes,
        setup=seed_base_ll,
        iterations=1,
        rounds=100
    )


def test_benchmarking_doubly_linked_list_palindrome_detection(benchmark):
    benchmark.pedantic(
        check_if_palindrome,
        setup=build_dl_palindrome,
        iterations=1,
        rounds=100
    )


def test_benchmarking_singly_linked_list_palindrome_detection(benchmark):
    benchmark.pedantic(
        check_if_palindrome,
        setup=build_sl_palindrome,
        iterations=1,
        rounds=100
    )
