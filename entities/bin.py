from _types.node_types import NODE_TYPES
from .base import Node


class Bin(Node):
    type = NODE_TYPES.BIN

    def __init__(self, name, content='') -> None:
        self._content = content
        super().__init__(name)

    @property
    def content(self):
        # return buffer content
        return self._content

    @content.setter
    def content(self, _):
        # check so content is not changed
        return self._content
