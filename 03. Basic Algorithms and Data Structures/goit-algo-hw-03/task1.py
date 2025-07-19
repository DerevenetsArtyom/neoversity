from pathlib import Path
import argparse
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description="Copy files and sort by extensions.")
    parser.add_argument("-s", "--source", type=Path, required=True, help="Path to the source directory")
    parser.add_argument("-d", "--dest", type=Path, default=Path("dist"), help="Path to the destination directory")
    return parser.parse_args()


def recursive_copy_files(src, dst):
    try:
        for item in src.iterdir():
            print(f'\nitem: "{item}"')
            if item.is_dir():
                recursive_copy_files(item, dst)  # Recursive call for subdirectories
            else:
                extension = item.suffix.lower()[1:]  # Get file extension
                if extension:
                    extension_dir = dst / extension
                    print(f'extension ".{extension}" --> "{extension_dir}/"')
                    extension_dir.mkdir(parents=True, exist_ok=True)  # Create subdirectory if not exist
                    dest_file = extension_dir / item.name
                    print(f'Copying "{item}" to "{dest_file}"')
                    shutil.copy(item, dest_file)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error copying files: {e}")


def main():
    args = parse_args()

    if not args.source.exists() or not args.source.is_dir():
        print(f"Error: The source directory '{args.source}' does not exist or is not a directory.")
        return

    print(f"\t ### Source: {args.source}, Destination: {args.dest} ### ")

    try:
        args.dest.mkdir(parents=True, exist_ok=True)  # Create destination directory if it doesn't exist
    except Exception as e:
        print(f"Failed to create output directory: {e}")
        return

    recursive_copy_files(args.source, args.dest)

    print(f"\n\t ### Files successfully copied to {args.dest} ### ")


if __name__ == "__main__":
    main()
