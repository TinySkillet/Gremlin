import os
from config import FILE_CHARACTER_LIMIT


def get_file_content(working_directory, file_path):

    joined_path = os.path.join(working_directory, file_path)
    parent_dir = os.path.realpath(working_directory)
    full_file_path = os.path.realpath(joined_path)

    if not full_file_path.startswith(parent_dir):
        return f'Error: Cannot read "{joined_path} as it is outside the permitted working directory'

    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{joined_path}'

    try:
        with open(full_file_path, "r") as f:
            content = f.read()
            if len(content) > FILE_CHARACTER_LIMIT:
                end_text = f'[...File "{joined_path} truncated at 10000 characters]'
                content = content[:FILE_CHARACTER_LIMIT] + end_text
            return content

    except Exception as e:
        return f"Error: An error occurred while trying to read from file: {joined_path}: {e}"
