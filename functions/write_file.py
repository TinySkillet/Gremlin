import os


def write_file(working_directory, file_path, content):

    joined_path = os.path.join(working_directory, file_path)
    parent_dir = os.path.realpath(working_directory)
    full_file_path = os.path.realpath(joined_path)

    if not full_file_path.startswith(parent_dir):
        return f'Error: Cannot write to "{joined_path}" as it is outside the permitted working directory'

    try:
        with open(full_file_path, "w") as f:
            f.write(content)
            return f"Successfully wrote to {joined_path} ({len(content)} characters written)"

    except Exception as e:
        return f"Error: An error occurred while trying to read from file: {joined_path}: {e}"
