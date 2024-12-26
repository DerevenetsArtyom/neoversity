"""Module for asynchronous sorting of files from source folder based on file extension"""

import argparse
import asyncio
import logging
from pathlib import Path

import aiofiles
import aiofiles.os
from aiopath import AsyncPath
from aioshutil import copyfile

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")


async def read_folder(src: Path, dst: Path) -> None:
    """Recursive function to parse files in the dir and to copy them into the destination dir based on file extension."""
    tasks = []

    async def recursive_read_folder(current_src: Path | AsyncPath) -> None:
        entries = await aiofiles.os.scandir(current_src)

        for entry in entries:
            if entry.is_file():
                tasks.append(asyncio.create_task(copy_file(AsyncPath(entry.path), dst)))
            elif entry.is_dir():
                await recursive_read_folder(AsyncPath(entry.path))

    await recursive_read_folder(src)
    await asyncio.gather(*tasks)


async def copy_file(src_file: AsyncPath, dst_folder: AsyncPath) -> None:
    """Function to copy the selected file to the destination folder based on the file extension."""
    try:
        extension = src_file.suffix[1:] if src_file.suffix else "no_extension"
        if await src_file.exists():
            target_folder = AsyncPath(dst_folder / extension)
            await target_folder.mkdir(exist_ok=True, parents=True)
            await copyfile(src_file, target_folder / src_file.name)
    except (PermissionError, OSError, IOError) as err:
        logging.error("Error copying file %s to %s: %s", src_file, dst_folder, err)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sort files from a folder into subfolders in a new folder based on file extension"
    )
    parser.add_argument("--source", type=Path, help="Source folder to read files from")
    parser.add_argument(
        "--destination",
        default="sorted_files",
        type=Path,
        help="Destination folder to copy files to",
    )
    args = parser.parse_args()

    src_folder = args.source.resolve()
    dst_folder = args.destination.resolve()

    if not src_folder.is_dir():
        logging.error("Source folder %s does not exist or is not a directory", src_folder)
        return

    asyncio.run(read_folder(src_folder, dst_folder))

    print(f"Files from folder '{src_folder}' are sorted and copied to '{dst_folder}'")


if __name__ == "__main__":
    main()
