import os
import subprocess
import sys
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    # path setup
    wd_path = os.path.abspath(working_directory)
    file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    # return errors for invalid inputs
    if not file_abs_path.startswith(wd_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_abs_path):
        return f'Error: File "{file_path}" not found.'
    if not file_abs_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    # logic
    try:
        process = [sys.executable, file_abs_path]
        result = subprocess.run(process + args, timeout=30, capture_output=True, text=True, cwd=wd_path)
        output = ''
        if result.stdout:
            output += f"STDOUT: {result.stdout}"
        if result.stderr:
            output += f"STDERR: {result.stderr}"
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}"
        if len(output) == 0:
            return f"No output produced"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),
        },
    ),
)