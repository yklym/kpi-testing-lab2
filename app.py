from entities import Dir, Bin, Buff, Log
# from helpers.tree import move_file


def main():
    root = Dir('root')

    dir_one = Dir('dir_one')
    dir_two = Dir('dir_two')

    root.insert_node(dir_one)
    root.insert_node(dir_two)

    dir_one.insert_node(Buff('buffer_one'))
    dir_one.insert_node(Log('log.txt'))
    dir_one.insert_node(Bin('bin', 'some content'))

    dir_two.insert_node(Buff('buffer_two'))
    dir_two.insert_node(Log('another_log.txt'))
    dir_two.insert_node(Bin('bin', 'some content 2'))

    print('ROOT folder:')
    root.list_children()

    print('\nFOLDER ONE')
    dir_one.list_children()

    print('\nFOLDER TWO')
    dir_two.list_children()

    return 0


if __name__ == '__main__':
    main()
