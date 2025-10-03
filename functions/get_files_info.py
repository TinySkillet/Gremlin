import os


def get_files_info(working_directory, directory="."):

    parent_dir = os.path.realpath(working_directory)
    print(parent_dir)
    unsafe_full_path = os.path.join(parent_dir, directory)
    child_dir = os.path.realpath(unsafe_full_path)

    # Security check to prevent directory traversal. Ensures the requested
    # directory is a subdirectory of the allowed parent directory.
    common_path = os.path.commonpath([parent_dir, child_dir])

    if common_path != parent_dir:
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

    if not os.path.isdir(child_dir):
        return f"Error: '{directory}' is not a directory"

    files_str = ""
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

            files_str += file_description

    except PermissionError:
        desc = f"Error: Permission error while trying to list contents of directory: {child_dir}\n"
        files_str += desc

    except Exception as e:
        desc = f"Error: An exception occurred: {e}\n"
        files_str += desc

    return files_str


if __name__ == "__main__":
    files_info = get_files_info(".", directory="calculator")
    print(files_info)
