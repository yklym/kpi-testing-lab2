from entities import Bin
from _types import NODE_TYPES


class TestBin:
    def test_node_name(self):
        filename = 'file.py'
        node = Bin(filename)
        assert hasattr(node, 'name')
        assert node.name == filename

    def test_node_type(self):
        node = Bin('')
        assert hasattr(node, 'type')
        assert node.type == NODE_TYPES.BIN

    def test_read_file(self):
        test_content = 'test_bin_content'
        node = Bin('', test_content)

        # check initialization
        assert hasattr(node, 'content')
        assert isinstance(node.content, str)
        assert node.content == test_content

        # check if can't update

        node.content = 'some bullshit'
        assert node.content != test_content
