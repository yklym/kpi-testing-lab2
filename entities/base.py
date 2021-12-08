from _types import NODE_TYPES


class Node:
    type = NODE_TYPES.BASE
    parent = None

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self):
        return f'{self.type}--> {self.name}'
