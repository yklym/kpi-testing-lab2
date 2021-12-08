from _types import NODE_TYPES, STATUSES
from .base import Node
from config import MAX_BUF_FILE_SIZE


class Buff(Node):
    type = NODE_TYPES.BUFF
    _content = []

    def __init__(self, name) -> None:
        self._content = []
        super().__init__(name)

    def push(self, line):
        if len(self._content) >= MAX_BUF_FILE_SIZE:
            return STATUSES.OVERFLOW
        self._content.append(line)
        return STATUSES.OK

    def pop(self):
        if not len(self._content):
            return None

        target_line = self._content[0]
        self._content = self._content[1:]
        return target_line
