from google.genai import types
from config import WORKING_DIR
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name

    # print function call details
    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")

    func = None
    match function_name:
        case "run_python_file":
            func = run_python_file
            # print(run_python_file(WORKING_DIR, file_path=function_call_part.args["file_path"]))
        case "get_file_content":
            func = get_file_content
            # print(get_file_content(WORKING_DIR, file_path=function_call_part.args["file_path"]))
        case "get_files_info":
            func = get_files_info
            # print(get_files_info(WORKING_DIR, directory=function_call_part.args["directory"]))
        case "write_file":
            func = write_file
            # print(write_file(WORKING_DIR, file_path=function_call_part.args["file_path"], content=function_call_part.args["content"]))
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )
        
    args = dict(function_call_part.args)
    args["working_directory"] = WORKING_DIR
    function_result = func(**args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
