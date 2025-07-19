from main import insert, AVL_TREE_KEYS


def sum_values(node):
    if not node:
        return 0
    return node.key + sum_values(node.left) + sum_values(node.right)


if __name__ == "__main__":
    root = None

    for key in AVL_TREE_KEYS:
        root = insert(root, key)

    print("The summ of all values in AVL tree:", sum_values(root))
