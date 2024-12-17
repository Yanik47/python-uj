import pytest
from singleList import SingleList
from node import Node

def test_insert_head():
    s_list = SingleList()
    s_list.insert_head(Node(1))
    assert s_list.head.data == 1
    assert s_list.tail.data == 1
    assert s_list.count() == 1

    s_list.insert_head(Node(2))
    assert s_list.head.data == 2
    assert s_list.tail.data == 1
    assert s_list.count() == 2

def test_insert_tail():
    s_list = SingleList()
    s_list.insert_tail(Node(1))
    assert s_list.head.data == 1
    assert s_list.tail.data == 1
    assert s_list.count() == 1

    s_list.insert_tail(Node(2))
    assert s_list.tail.data == 2
    assert s_list.count() == 2

def test_remove_head():
    s_list = SingleList()
    s_list.insert_tail(Node(1))
    s_list.insert_tail(Node(2))

    removed = s_list.remove_head()
    assert removed.data == 1
    assert s_list.head.data == 2
    assert s_list.count() == 1

    removed = s_list.remove_head()
    assert removed.data == 2
    assert s_list.is_empty()

    with pytest.raises(ValueError):
        s_list.remove_head()

def test_remove_tail():
    s_list = SingleList()
    s_list.insert_tail(Node(1))
    s_list.insert_tail(Node(2))

    removed = s_list.remove_tail()
    assert removed.data == 2
    assert s_list.tail.data == 1
    assert s_list.count() == 1

    removed = s_list.remove_tail()
    assert removed.data == 1
    assert s_list.is_empty()

    with pytest.raises(ValueError):
        s_list.remove_tail()

def test_join():
    list1 = SingleList()
    list2 = SingleList()

    list1.insert_tail(Node(1))
    list1.insert_tail(Node(2))

    list2.insert_tail(Node(3))
    list2.insert_tail(Node(4))

    list1.join(list2)

    assert list1.count() == 4
    assert list1.head.data == 1
    assert list1.tail.data == 4

    assert list2.is_empty()

def test_clear():
    s_list = SingleList()
    s_list.insert_tail(Node(1))
    s_list.insert_tail(Node(2))
    s_list.insert_tail(Node(3))

    s_list.clear()
    assert s_list.is_empty()
    assert s_list.count() == 0

def test_iter():
    s_list = SingleList()
    s_list.insert_tail(Node(1))
    s_list.insert_tail(Node(2))
    s_list.insert_tail(Node(3))

    result = [data for data in s_list]
    assert result == [1, 2, 3]

def test_str():
    s_list = SingleList()
    s_list.insert_tail(Node(1))
    s_list.insert_tail(Node(2))
    s_list.insert_tail(Node(3))

    assert str(s_list) == "1 -> 2 -> 3"
