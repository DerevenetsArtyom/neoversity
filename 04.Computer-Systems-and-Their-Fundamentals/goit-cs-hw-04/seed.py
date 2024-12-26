"""Module to create and populate files with randomly generated text in the specific folder"""

import os
from faker import Faker

FILES = 50
LENGTH = 2000
DIRECTORY = "src"

fake = Faker()


def main(num_files: int = FILES, text_length: int = LENGTH, directory: str = DIRECTORY):
    """Function to create a directory and populate it with files with fake text"""
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(1, num_files + 1):
        file_path = os.path.join(directory, f"file{i}.txt")
        with open(file_path, "w", encoding="UTF-8") as fd:
            fd.write(fake.text(max_nb_chars=text_length))

    print(f"Seeded {num_files} files with random text in the '{directory}' directory")


if __name__ == "__main__":
    main()
