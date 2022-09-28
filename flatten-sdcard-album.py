import os
import re
import sys

# File names are in "YYDDMMHHmmSS-<some HEX value>" format.
pattern = re.compile(r'(.{4})(.{2})(.{2})(.{2})(.{2})(.{2}).*\.(.{3})')


def flatten_and_rename(current_dir):
    for item in os.listdir(current_dir):
        current_item = os.path.join(current_dir, item)
        if os.path.isdir(current_item):
            flatten_and_rename(current_item)
        else:
            m = pattern.match(item)
            # TODO: make sure to not overwrite if two files were made in the same second
            new_name = os.path.join(
                working_dir,
                (f'{m.group(1)}-{m.group(2)}-{m.group(3)}_'
                 f'{m.group(4)}-{m.group(5)}-{m.group(6)}.{m.group(7)}')
            )
            os.rename(current_item, new_name)
            print(f'{current_item} -> {new_name}')


if __name__ == "__main__":
    working_dir = (sys.argv[1] if len(sys.argv) > 1 else '.')
    print(f'Current working dir is "{working_dir}"')
    flatten_and_rename(working_dir)
