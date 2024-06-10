import json

def read_jrnl_file(jrnl_file_path):
    with open(jrnl_file_path, 'r') as file:
        content = file.read()
        if content.strip():
            entries = json.load(file)
        else:
            print("The JSON file is empty or only contains whitespace")

    return entries
