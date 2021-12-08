from entities import Node
from _types import NODE_TYPES


class TestNode:
    def test_node_name(self):
        filename = 'file.py'
        node = Node(filename)
        assert hasattr(node, 'name')
        assert node.name == filename

    def test_node_type(self):
        node = Node('')
        assert hasattr(node, 'type')
        assert node.type == NODE_TYPES.BASE

    def test_parent(self):
        node = Node('')
        assert hasattr(node, 'parent')
        assert node.parent == None

    def test_print(self):
        filename = 'file.py'
        node = Node(filename)
        assert str(node) == f'{NODE_TYPES.BASE}--> {filename}'
