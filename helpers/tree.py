def move_file(source, target, filename):
    target_node = source.get_child(filename)
    print('target_node', target_node)
    source.remove_node(filename)
    target.insert_node(target_node)
