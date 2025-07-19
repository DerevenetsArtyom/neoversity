import sys
from pathlib import Path
from colorama import init, Fore, Back

# Initializing colorama to support color output
init(autoreset=True)


def display_directory_structure(directory_path: str, indent: int = 0) -> None:
    """Display nested files and files recursively."""

    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"The path '{directory_path}' doesn't exist or is not a directory.")
        return

    # Show a special icon for the selected folder
    if indent == 0:
        print(" " * indent + Fore.BLUE + f"📦 " + path.absolute().name)

    # Iterate over all files and subdirectories
    for item in path.iterdir():
        if item.is_dir():
            print(" " * (indent + 2) + Fore.CYAN + f"📁 {item.name}/")
            display_directory_structure(item, indent + 4)
        elif item.is_file():
            print(" " * (indent + 2) + Fore.YELLOW + f"📜 {item.name}")


if __name__ == "__main__":
    # Check arguments validity
    if len(sys.argv) != 2:
        print(Fore.RED + "Specify the path to the directory.")
        sys.exit(1)

    # Get the desired directory path
    directory_path = sys.argv[1]

    display_directory_structure(directory_path)
