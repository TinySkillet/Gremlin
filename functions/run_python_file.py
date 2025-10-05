import os
import subprocess
import sys


def run_python_file(working_directory, file_path: str, args=[]):

    joined_path = os.path.join(working_directory, file_path)
    parent_dir = os.path.realpath(working_directory)

    full_file_path = os.path.realpath(joined_path)

    if not full_file_path.startswith(parent_dir):
        return f'Error: Cannot execute "{joined_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_file_path):
        return f'Error: File: "{joined_path}" not found.'

    if not file_path.endswith(".py"):
        return f"Error: {joined_path} is not a Python file."

    commands = [sys.executable, full_file_path]

    if args:
        commands.extend(args)
    try:
        process_obj = subprocess.run(
            commands,
            timeout=30,
            capture_output=True,
            text=True,
        )
        stdout = f"STDOUT: {process_obj.stdout}"
        stderr = f"STDERR: {process_obj.stderr}"

        formatted_string = "\n".join([stdout, stderr])

        if process_obj.returncode != 0:
            formatted_string += f"\nProcess exited with code {process_obj.returncode}"

        # if we get a zero return code but no output
        if not stdout:
            return "No output produced"

        return formatted_string

    except Exception as e:
        return f"Error: executing Python file: {e}"
