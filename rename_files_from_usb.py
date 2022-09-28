"""
Will rename the files in their respective subfolders
into `YYYY-MM-DD_HH-mm-SS<suffix>` format, keeping their original extensions.
"""

import os
import re
import sys

# File names are in "YYMMDDHHmmSSxx_c" format.
pattern = re.compile(r'(.{4})(.{2})(.{2})(.{2})(.{2})(.{2})(.*)\.(.{3})')


def rename_usb_album(current_dir):
    """Traverse subdirectories and rename mathing files."""
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            for file_name in os.listdir(item_path):
                file_path = os.path.join(item_path, file_name)

                match = pattern.match(file_name)
                if not match:
                    print(f'Skipping "{file_path}": unexpected name format.')
                    continue

                new_name = os.path.join(
                    item_path,
                    (f'{match.group(1)}-{match.group(2)}-{match.group(3)}_'
                     f'{match.group(4)}-{match.group(5)}-{match.group(6)}_{match.group(7)}'
                     f'.{match.group(8)}')
                )

                os.rename(file_path, new_name)
                print(f'{file_path} -> {new_name}')
        else:
            print(f'Skipping "{item_path}": not a directory.')


if __name__ == "__main__":
    working_dir = (sys.argv[1] if len(sys.argv) > 1 else '.')
    print(f'Current working dir is "{working_dir}"')
    rename_usb_album(working_dir)
