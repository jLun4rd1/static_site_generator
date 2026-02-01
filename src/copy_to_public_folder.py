import os
import shutil


PUBLIC_PATH = "public/"
STATIC_PATH = "static/"

def copy_to_public_folder():
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)
    os.mkdir(PUBLIC_PATH)
    _copy_from_static(STATIC_PATH)

def _copy_from_static(file_path):
    if os.path.isfile(file_path):
        file_suffix = file_path.split(STATIC_PATH)[1]
        file_destination = os.path.join(PUBLIC_PATH, file_suffix)
        shutil.copy(file_path, file_destination)
        return
    else:
        if file_path != STATIC_PATH:
            folder_suffix = file_path.split(STATIC_PATH)[1]
            public_folder_path = os.path.join(PUBLIC_PATH, folder_suffix)
            os.mkdir(public_folder_path)
        all_files = os.listdir(file_path)
        for file in all_files:
            _copy_from_static(os.path.join(file_path, file))