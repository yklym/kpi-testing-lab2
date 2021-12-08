from _types.node_types import NODE_TYPES
from .base import Node


class Log(Node):
    type = NODE_TYPES.LOG
    _content = []

    def __init__(self, name) -> None:
        self._content = []

        super().__init__(name)

    @property
    def content(self):
        # return log content
        return '\n'.join(self._content)

    @content.setter
    def content(self):
        # check so content is not changed
        return self._content

    def add_line(self, line):
        self._content.append(line)
        return self.content
