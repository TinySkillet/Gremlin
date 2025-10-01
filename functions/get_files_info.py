import os


def get_files_info(working_directory, directory="."):

    work_dir = os.path.abspath(working_directory)
    target_directory = os.path.join(work_dir, directory)
    target_dir = os.path.abspath(target_directory)

    print("Working Directory: ", working_directory)
    print("Abs working directory: ", work_dir)

    print("Target directory: ", target_directory)
    print("Abs target directory", target_dir)

    # if not target_dir.startswith(work_dir):
    #     f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # if not os.path.isdir(target_dir):
    #     f'Error: "{directory}" is not a directory'


if __name__ == "__main__":
    working_dir = "/home/tinyskillet/Src/Gremlin"
    get_files_info(working_directory=working_dir)
