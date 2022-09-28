import os
import re
import sys

# File names are in "YYMMDDHHmmSSxx_c" format.
pattern = re.compile(r'(.{4})(.{2})(.{2})(.{2})(.{2})(.{2})(.*)\.(.{3})')


def rename_usb_album(current_dir):
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            for file_name in os.listdir(item_path):
                file_path = os.path.join(item_path, file_name)
                m = pattern.match(file_name)
                if m:
                    new_name = os.path.join(
                        item_path,
                        (f'{m.group(1)}-{m.group(2)}-{m.group(3)}_'
                        f'{m.group(4)}-{m.group(5)}-{m.group(6)}_{m.group(7)}'
                        f'.{m.group(8)}')
                    )
                    os.rename(file_path, new_name)
                    print(f'{file_path} -> {new_name}')
                else:
                    print(f'Skipping "{file_path}": unexpected name format.')
        else:
            print(f'Skipping "{item_path}": not a directory.')

if __name__ == "__main__":
    working_dir = (sys.argv[1] if len(sys.argv) > 1 else '.')
    print(f'Current working dir is "{working_dir}"')
    rename_usb_album(working_dir)
