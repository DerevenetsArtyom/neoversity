def get_cats_info(path: str) -> list[dict]:
    """Read cats' data from a file and return it as a dict."""

    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_item = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                cats_info.append(cat_item)

    except FileNotFoundError:
        print(f"The file is not found: {path} ")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return cats_info


# Example of usage
cats_info = get_cats_info("task_2/cats.txt")
print(cats_info)
