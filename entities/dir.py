from _types.node_types import NODE_TYPES
from config import DIR_MAX_ELEMS
from .base import Node


class Dir(Node):
    type = NODE_TYPES.DIR
    _children = []

    def __init__(self, name) -> None:
        self._children = []
        super().__init__(name)

    def insert_node(self, node: Node):
        is_size_exceeded = len(self._children) >= DIR_MAX_ELEMS
        is_existing_name = self.has_child(node.name)

        if not (is_existing_name or is_size_exceeded):
            self._children.append(node)
            node.parent = self

        return len(self._children)

    def remove_node(self, node_name: str):
        target_node = self.get_child(node_name)
        target_node.parent = None

        self._children = [
            node for node in self._children if node.name != node_name]
        return len(self.children)

    def list_children(self):
        # push elements list
        for node in self._children:
            print(node)

    def has_child(self, name):
        # for testing
        return any([node.name == name for node in self._children])

    def get_child(self, name):
        filtered = [node for node in self._children if node.name == name]
        if len(filtered):
            return filtered[0]
        return None

    @property
    def children(self):
        return self._children
