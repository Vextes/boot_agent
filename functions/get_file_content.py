import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    # path setup
    wd_path = os.path.abspath(working_directory)
    file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    # return errors for invalid directory inputs
    if not file_abs_path.startswith(wd_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_abs_path):
        f'Error: File not found or is not a regular file: "{file_path}"'

    # logic
    try:
        with open(file_abs_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if os.path.getsize(file_abs_path) > MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f"Error: {e}"