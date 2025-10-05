import os


def get_files_info(working_directory, directory="."):

    parent_dir = os.path.realpath(working_directory)
    unsafe_full_path = os.path.join(parent_dir, directory)
    child_dir = os.path.realpath(unsafe_full_path)

    # Security check to prevent directory traversal. Ensures the requested
    # directory is a subdirectory of the allowed parent directory.
    if not child_dir.startswith(parent_dir):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

    if not os.path.isdir(child_dir):
        return f"Error: '{directory}' is not a directory"

    response = ""
    try:
        files = os.listdir(child_dir)

        for index, file in enumerate(files):
            full_file_path = os.path.join(child_dir, file)
            size = os.path.getsize(full_file_path)

            if os.path.isdir(full_file_path):
                is_dir = True
            else:
                is_dir = False

            file_description = f"- {file}: file_size={size} bytes, is_dir={is_dir}"

            if index < len(files) - 1:
                file_description += "\n"

            response += file_description

    except PermissionError:
        desc = f"Error: Permission error while trying to list contents of directory: {child_dir}\n"
        response += desc

    except Exception as e:
        desc = f"Error: An exception occurred: {e}\n"
        response += desc

    return response
