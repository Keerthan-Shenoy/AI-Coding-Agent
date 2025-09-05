import os

def get_files_info(working_directory, directory="."):
    """Get information about files in the specified directory.
    Args:
        working_directory (str): The base working directory.
        directory (str): The target directory relative to the working directory.
    Returns:
        str: Information about files in the directory or an error message.
    """

    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_directory.startswith(abs_working_directory):
        return "Error: Directory is outside the working directory."
    
    final_response = ""
    contents = os.listdir(abs_directory)
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response += f'Name: {content}, Type: {"Directory" if is_dir else "File"}, Size: {size} bytes\n'

    return final_response