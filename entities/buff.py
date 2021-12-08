from _types.node_types import NODE_TYPES
from .base import Node


class Buff(Node):
    type = NODE_TYPES.BUFF
    _content = []

    def __init__(self, name) -> None:
        super().__init__(name)

    def push(self, line):
        # check MAX_BUF_FILE_SIZE
        # and push if needed
        return self

    def pop(self):
        return None
