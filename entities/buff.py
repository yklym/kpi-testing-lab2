from _types.node_types import NODE_TYPES
from .base import Node


class Buff(Node):
    type = NODE_TYPES.BUFF
    _content = []

    def __init__(self, name) -> None:
        super().__init__(name)

    @property
    def content(self):
        # return log _content
        return '\n'.join([f'{i}. {self._}' for i in range(len(self._content))])

    @content.setter
    def content(self):
        # check so _content is not changed
        return self._content

    def push(self, line):
        # check MAX_BUF_FILE_SIZE
        # and push if needed
        return self

    def pop(self):
        return None
