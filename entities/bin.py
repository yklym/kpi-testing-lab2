from _types.node_types import NODE_TYPES
from .base import Node


class Bin(Node):
    type = NODE_TYPES.BIN
    content = ''

    def __init__(self, name) -> None:
        super().__init__(name)

    @property
    def content(self):
        # return buffer content
        return self.content

    @content.setter
    def content(self):
        # check so content is not changed
        return self.content
