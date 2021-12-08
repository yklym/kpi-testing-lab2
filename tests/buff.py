from entities import Buff
from _types import NODE_TYPES, STATUSES
from config import MAX_BUF_FILE_SIZE


class TestBuff:
    def test_node_name(self):
        filename = 'file.py'
        node = Buff(filename)
        assert hasattr(node, 'name')
        assert node.name == filename

    def test_node_type(self):
        node = Buff('')
        assert hasattr(node, 'type')
        assert node.type == NODE_TYPES.BUFF

    def test_content(self):
        node = Buff('')

        # test push
        for i in range(MAX_BUF_FILE_SIZE):
            insert_status = node.push(f'line {i}')
            assert insert_status == STATUSES.OK

        # test overflow
        insert_status = node.push('line overflow')
        assert insert_status == STATUSES.OVERFLOW

        # test pop
        for i in range(MAX_BUF_FILE_SIZE):
            received_line = node.pop()
            assert received_line == f'line {i}'

        # pop empty buffer
        received_line = node.pop()
        assert received_line == None
