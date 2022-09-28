"""
Will move all the files from their respective subfolders into the `Album` folder
and rename them in `YYYY-MM-DD_HH-mm-SS` format, keeping their original extensions.
"""

import os
import re
import sys

# File names are in "YYDDMMHHmmSS-<some HEX value>" format.
pattern = re.compile(r'(.{4})(.{2})(.{2})(.{2})(.{2})(.{2}).*\.(.{3})')


def flatten_and_rename(current_dir, target_dir):
    """Traverse directories recursively and move matching files to `target_dir`."""
    for item in os.listdir(current_dir):
        current_item = os.path.join(current_dir, item)
        if os.path.isdir(current_item):
            flatten_and_rename(current_item, target_dir)
        else:
            match = pattern.match(item)
            if not match:
                print(f'Skipping "{current_item}": unexpected name format.')
                continue

            new_name = os.path.join(
                target_dir,
                (f'{match.group(1)}-{match.group(2)}-{match.group(3)}_'
                 f'{match.group(4)}-{match.group(5)}-{match.group(6)}.{match.group(7)}')
            )

            i = 0
            while os.path.exists(new_name):
                i += 1
                new_name = os.path.join(
                    target_dir,
                    (f'{match.group(1)}-{match.group(2)}-{match.group(3)}_'
                     f'{match.group(4)}-{match.group(5)}-{match.group(6)}-{i}.{match.group(7)}')
                )

            os.rename(current_item, new_name)
            print(f'{current_item} -> {new_name}')


if __name__ == "__main__":
    working_dir = (sys.argv[1] if len(sys.argv) > 1 else '.')
    print(f'Current working dir is "{working_dir}"')
    flatten_and_rename(working_dir, working_dir)
