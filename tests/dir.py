from entities import Dir, Node
from _types import NODE_TYPES
from config import DIR_MAX_ELEMS


class TestDir:
    def test_node_name(self):
        filename = 'file.py'
        node = Dir(filename)
        assert hasattr(node, 'name')
        assert node.name == filename

    def test_node_type(self):
        node = Dir('')
        assert hasattr(node, 'type')
        assert node.type == NODE_TYPES.DIR

    def test_child_check(self):
        dir_name = 'dir'
        dir_node = Dir(dir_name)
        child_name = 'child'
        node = Node(child_name)
        dir_node.insert_node(node)
        assert dir_node.has_child(child_name)

    def test_directory_insertion(self):
        dir_name = 'dir_i'
        dir_node = Dir(dir_name)

        # test normal insertion
        for i in range(DIR_MAX_ELEMS):
            child_name = f'node{i}'
            node = Node(child_name)

            inserted_amount = dir_node.insert_node(node)

            assert inserted_amount == i + 1
            assert node.parent != None
            assert node.parent.name == dir_name
            assert node.parent.has_child(child_name)

        # test we won't ovwrflow DIR_MAX_ELEMS
        child_name = f'node{DIR_MAX_ELEMS + 1}'
        overflow_node = Node(child_name)
        old_amount = DIR_MAX_ELEMS

        children_amount = dir_node.insert_node(overflow_node)

        assert children_amount == old_amount
        assert overflow_node.parent == None or node.parent.name != dir_name
        assert not node.parent.has_child(child_name)

    def test_insert_same_name(self):
        dir_name = 'dir'
        dir_node = Dir(dir_name)

        child_name = 'node'
        child_one = Node(child_name)
        child_two = Node(child_name)

        children_amount = dir_node.insert_node(child_one)
        assert children_amount == 1

        # use existing name
        children_amount = dir_node.insert_node(child_two)
        assert children_amount == 1

        # insert same node
        children_amount = dir_node.insert_node(child_one)
        assert children_amount == 1

    def test_removing_node(self):
        dir_name = 'dir'
        dir_node = Dir(dir_name)

        child_name = 'child'
        child_node = Node(child_name)
        dir_node.insert_node(child_node)

        children_amount = dir_node.remove_node(child_name)

        assert child_node.parent == None
        assert not dir_node.has_child(child_name)
        assert children_amount == 0
