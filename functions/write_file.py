import os
from google.genai import types

def write_file(working_directory, file_path, content):
    # path setup
    wd_path = os.path.abspath(working_directory)
    file_abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    # return errors for invalid directory inputs
    if not file_abs_path.startswith(wd_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_abs_path):
        try:
            os.makedirs(os.path.dirname(file_abs_path), exist_ok=True)
        except Exception as e:
            return f"Error: {e}"
        
    # logic
    try:
        with open(file_abs_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Adds the given content to the end of the specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the file.",
            ),
        },
    ),
)