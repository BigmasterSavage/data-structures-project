import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.LinkedList = LinkedList()

    def test_insert_beginning(self):
        self.LinkedList.insert_beginning({'id': 1})
        self.assertEqual(str(self.LinkedList), "{'id': 1} -> None")
        self.LinkedList.insert_beginning({'id': 2})
        self.assertEqual(str(self.LinkedList), "{'id': 2} -> {'id': 1} -> None")

    def test_insert_at_end(self):
        self.LinkedList.insert_at_end({'id': 2})
        self.assertEqual(str(self.LinkedList), "{'id': 2} -> None")
        self.LinkedList.insert_at_end({'id': 3})
        self.assertEqual(str(self.LinkedList), "{'id': 2} -> {'id': 3} -> None")

    def test_list(self):
        self.LinkedList.insert_beginning({'id': 1})
        self.LinkedList.insert_at_end({'id': 2})
        self.LinkedList.insert_at_end({'id': 3})
        lst = LinkedList.to_list(self.LinkedList)
        self.assertEqual(lst, [{'id': 1}, {'id': 2}, {'id': 3}])

    def test_get_data_by_id(self):
        self.LinkedList.insert_beginning({'id': 1})
        self.LinkedList.insert_at_end({'id': 2})
        self.LinkedList.insert_at_end({'id': 3})
        user_data = self.LinkedList.get_data_by_id(3)
        self.assertEqual(user_data, {'id': 3})

    def test_try_except(self):
        self.LinkedList.insert_at_end({'id': 1})
        self.LinkedList.insert_at_end('idusername')
        self.assertRaises(TypeError, 'Данные не являются словарем или в словаре нет id')