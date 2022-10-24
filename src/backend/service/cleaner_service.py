import os
import tempfile
import glob


def delete_temp_files(suffix):
    temp_dir = tempfile.gettempdir()
    file_list = glob.glob(f'{temp_dir}\IMAGE_MANIPULATOR*{suffix}', recursive=True)
    for file in file_list:
        print(f'Removing file: {file}')
        os.remove(file)
    file_list = glob.glob(f'{temp_dir}\IMAGE_MANIPULATOR*{suffix}', recursive=True)
    print(f'File list after cleanup: {file_list}')