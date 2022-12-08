import shutil
import sys
import os
from pathlib import Path
from .sort_file import name_folders, sort_files
from .sort_folder import sort_folders


def clean():
    try:
        path_folder = Path(sys.argv[1])
    except IndexError:
        print("No path(")
        return None

    if not path_folder.exists():
        print("Path is not exist")
        return None

    list_path = list(path_folder.iterdir())
    for new_folder in name_folders:
        path_new_dir = os.path.join(path_folder, new_folder)
        if not os.path.exists(path_new_dir):
            os.makedirs(path_new_dir)
        else:
            print("This folder already exists", path_new_dir)
    for any_path in list_path:
        if any_path.is_dir():
            sort_folders(any_path)
            if any_path.name in name_folders:
                continue
            else:
                shutil.rmtree(any_path)
        else:
            sort_files(any_path)
    list_sort_done = list(path_folder.iterdir())
    # print("You're welcome.\n", list_sort_done)
    print("You're welcome.")


if __name__ == "__main__":
    clean()