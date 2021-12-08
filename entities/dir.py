from _types.node_types import NODE_TYPES
from .base import Node


class Dir(Node):
    type = NODE_TYPES.DIR
    _children = []

    def __init__(self, name) -> None:
        super().__init__(name)

    def insert_node(self, node: Node):
        # check if size not excided and name is not taken
        # Then insert node
        pass

    def remove_node(self, node_name: str):
        # find node with appropriate name and remove
        return self.children

    def list_children(self):
        # push elements list
        pass

    def has_child(self, name):
        # for testing
        return any([node.name == name for node in self._children])
