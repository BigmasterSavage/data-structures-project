"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
import random
from src.stack import Node, Stack


class SrcTest(unittest.TestCase):
    new_data = random.randint(10, 20)
    zero_node = Node(random.randint(1, 10), None)

    def setUp(self):
        self.Stack = Stack()

    def test_correct_zero_node_init(self):
        self.assertFalse(self.zero_node.next_node)
        self.assertTrue(self.zero_node.data)

    def test_param(self):
        n1 = self.zero_node
        n2 = Node(random.randint(11, 20), n1)
        self.assertNotEqual(n1.data, n2.data)
        self.assertEquals(n1, n2.next_node)

    def test_correct_stack_init(self):
        self.assertFalse(self.Stack.top)

    def test_push(self):
        top_0 = self.Stack
        top_0.push(self.new_data)
        self.assertEquals(top_0.top.data, self.new_data)

    def test_pop(self):
        top_0 = self.Stack
        top_0.push(self.new_data)
        top_0.pop()
        self.assertFalse(top_0.top)

    def test_str(self):
        top_0 = self.Stack
        top_0.push(self.new_data)
        self.assertEquals(str(top_0), str(self.new_data))

