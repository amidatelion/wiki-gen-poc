import os
def process_files(primary_path, secondary_path, prefix):
    file_dict = {}
    def add_file_contents(file_path, directory, file_dict, current_file_lines):
        # Read file and get its contents
        with open(os.path.join(directory, file_path), 'r') as file:
            lines = file.readlines()
        # Iterate over the lines in the file
        for line in lines:
            line = line.strip()
            current_file_lines.append(line)
            # If the line starts with the prefix, use the entire line as the file name
            if line.startswith(prefix):
                referenced_file = line  # Use the whole line as the file name
                # Check if the referenced file exists in the secondary path
                if os.path.isfile(os.path.join(secondary_path, referenced_file)):
                    # Recursively add the contents of the referenced file
                    add_file_contents(referenced_file, secondary_path, file_dict, current_file_lines)
    # Iterate through files in primary path and process each
    for file_name in os.listdir(primary_path):
        if os.path.isfile(os.path.join(primary_path, file_name)):
            file_dict[file_name] = []
            add_file_contents(file_name, primary_path, file_dict, file_dict[file_name])
    return file_dict