class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data, self.top)
        self.top = node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        pop = self.top.data
        self.top = self.top.next_node
        return pop

    def __str__(self):
        """Дандер метод для строкового представления объекта"""
        node = self.top
        if node is None:
            return str(None)
        full = []
        while node:
            full.append(str(node.data))
            node = node.next_node
        return "\n".join(full)