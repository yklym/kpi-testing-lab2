from entities import Bin, Dir, Bin
from _types import NODE_TYPES
from helpers.tree import move_file


class TestTree:
    def test_moving_nodes(self):
        dir_node = Dir('root')
        dir_one = Dir('dir_one')
        dir_two = Dir('dir_two')

        bin_name = 'bin'
        test_file = Bin(bin_name, bin_name)

        dir_node.insert_node(dir_one)
        dir_node.insert_node(dir_two)

        dir_one.insert_node(test_file)

        move_file(dir_one, dir_two, bin_name)

        assert not dir_one.has_child(bin_name)
        assert dir_two.has_child(bin_name)
        assert test_file.parent.name == dir_two.name
