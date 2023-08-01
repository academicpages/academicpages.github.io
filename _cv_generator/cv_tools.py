
import re
import os

# Define functions used in script
def edit_citation_keys(bib_file_path):
    with open(bib_file_path, 'r') as bib_file:
        bib_data = bib_file.readlines()

    modified_bib_data = []
    for line in bib_data:
        if line.startswith('@'):
            # Extract the citation key from the line
            start_index = line.find('{') + 1
            end_index = line.find(',')
            citation_key = line[start_index:end_index].strip()

            # Remove spaces and periods from the citation key using regex
            citation_key = re.sub(r'[ .]', '', citation_key)

            # Modify the line with the updated citation key
            line = line[:start_index] + citation_key + line[end_index:]

        modified_bib_data.append(line)

    # Save the modified .bib file
    with open(bib_file_path, 'w') as bib_file:
        bib_file.writelines(modified_bib_data)

def delete_files_in_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory path.")
        return

    file_list = os.listdir(directory_path)
    for file_name in file_list:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except OSError as e:
                print(f"Error while deleting file: {file_path}\n{e}")

def insert_string_before_last_brace(input_string, insert_string):
    '''
    Parameters
    ----------
    s : str
        original string
    inster_string : str
        string to insert
    '''
    last_brace_index = input_string.rfind('}')
    if last_brace_index != -1:
        modified_string = input_string[:last_brace_index] + insert_string + input_string[last_brace_index:]
        return modified_string
    else:
        return [input_string]