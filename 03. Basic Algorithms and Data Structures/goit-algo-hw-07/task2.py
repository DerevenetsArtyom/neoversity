from main import insert, min_value_node, AVL_TREE_KEYS


# Function to find the minimum value in the AVL tree
def find_min(node):
    return min_value_node(node).key  # Use the min_value_node function to find and return the minimum key


# Example usage
if __name__ == "__main__":
    root = None  # Initialize the root of the AVL tree as None

    for key in AVL_TREE_KEYS:
        root = insert(root, key)  # Insert each key into the AVL tree

    print("The minimum value in the AVL tree:", find_min(root))  # Find and print the minimum value in the AVL tree
