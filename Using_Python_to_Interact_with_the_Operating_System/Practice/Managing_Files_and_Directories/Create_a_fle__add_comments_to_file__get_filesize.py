import os


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as my_file:
        my_file.write(comments)
    file_size = os.path.getsize(filename)
    return file_size


print(create_python_script("program.py"))
