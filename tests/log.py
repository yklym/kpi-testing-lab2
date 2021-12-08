from entities import Log
from _types import NODE_TYPES


class TestLog:
    def test_node_name(self):
        filename = 'file.py'
        node = Log(filename)
        assert hasattr(node, 'name')
        assert node.name == filename

    def test_node_type(self):
        node = Log('')
        assert hasattr(node, 'type')
        assert node.type == NODE_TYPES.LOG

    def test_read_file(self):
        node = Log('')
        assert hasattr(node, 'content')
        assert isinstance(node.content, str)

    def test_adding_lines(self):
        node = Log('')
        test_str = 'line1'
        node.add_line(test_str)

        assert node.content == test_str

        node.add_line(test_str)

        assert node.content == test_str + '\n' + test_str
        assert len(node.content.split('\n')) == 2
