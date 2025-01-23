# Date: 11/29/2024
# Brady Johnson
# IDE: Pycharm
# Tested on:
# System Type: ARM-64 base (Apple Silicon)
# macOSSequoia v15.1
# Microsoft Windows 11 pro v10.0.26631 Build:22631 (virtual)
#

# I did not see the need to use the os import.
import platform


def get_current_os():
    os_name = platform.system()
    return os_name

def convert_path(os_name, path):
    if os_name == "Windows":
        if path.startswith("/"):    # I am making the assumption that all given file paths will go down to the root.
            path = path.replace("/", f"C:\\", 1)
        path =  path.replace("/", "\\")
        path = path.replace("\ ", " ") # Deal with hold over escape sequences
        path = path.replace("` ", " ")  # Deal with hold over escape sequences
        path = path.replace(" ", "` ")  # Deal with potential spaces in the name
        return path

    elif os_name == "Darwin":
        if path.startswith("C:\\"):     # assuming all given file paths go down to the root.
            path = path.replace(f"C:\\", "/")
        path = path.replace("\\", "/")  # "/" is the representative for "Macintosh HD" when creating a path.
        path = path.replace("` ", " ")  # Deal with hold over escape sequences
        path = path.replace("\ ", " ")  # Deal with hold over escape sequences
        path = path.replace(" ", "\ ")  # Deal with potential spaces in the name
        return path
    else:
        raise ValueError("Unsupported operating system")

if __name__ == "__main__":
    current_os = get_current_os()
    user_input_path = input("Please enter the file name and path (example: /Users/bjohn323/GitHub/test.txt): ")
    try:
        converted_path = convert_path(current_os, user_input_path)
        print(f"The converted file path is: {converted_path}")
    except ValueError as e:
        print(e)




