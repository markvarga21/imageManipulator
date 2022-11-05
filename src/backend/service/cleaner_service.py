import os
import tempfile
import glob


def delete_temp_files(suffix: str) -> None:
    temp_dir = tempfile.gettempdir()
    file_list = glob.glob(f'{temp_dir}{os.sep}IMAGE_MANIPULATOR*{suffix}', recursive=True)
    for file in file_list:
        print(f'Removing file: {file}')
        os.remove(file)
    file_list = glob.glob(f'{temp_dir}{os.sep}IMAGE_MANIPULATOR*{suffix}', recursive=True)
    print(f'File list after cleanup: {file_list}')


def clean_output_for_user(user_name: str) -> None:
    path = os.path.join(os.getcwd(), 'resources', 'output')
    output_files = glob.glob(f'{path}{os.sep}OCR_{user_name}*', recursive=True)
    for file in output_files:
        os.remove(file)

def clean_retouch_output_for_user(user_name: str) -> None:
    path = os.path.join(os.getcwd(), 'resources', 'output')
    output_files = glob.glob(f'{path}{os.sep}RETOUCH_{user_name}*', recursive=True)
    for file in output_files:
        os.remove(file)
