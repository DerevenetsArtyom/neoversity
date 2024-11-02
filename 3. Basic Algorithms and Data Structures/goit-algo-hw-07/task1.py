from main import insert, AVL_TREE_KEYS


# Function to find the maximum value in the AVL tree
def find_max(node):
    current = node  # Start from the given node
    while current.right is not None:  # Traverse to the rightmost node
        current = current.right
    return current.key  # Return the key of the rightmost node


# Example usage
if __name__ == "__main__":
    root = None  # Initialize the root of the AVL tree as None

    for key in AVL_TREE_KEYS:
        root = insert(root, key)  # Insert each key into the AVL tree

    print("The maximum value in the AVL tree:", find_max(root))  # Find and print the maximum value in the AVL tree
