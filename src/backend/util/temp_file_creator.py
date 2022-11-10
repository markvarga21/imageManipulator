import tempfile


def return_temp_file(suffix: str) -> tempfile.TemporaryFile:
    temp_file = tempfile.TemporaryFile(
        mode='r+', suffix=suffix, prefix='IMAGE_MANIPULATOR', delete=False)
    return temp_file
