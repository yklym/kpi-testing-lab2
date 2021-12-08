from _types import NODE_TYPES


class Node:
    type = NODE_TYPES.BASE
    parent_dir = None 
    
    def __init__(self, name) -> None:
        self.name = name
