import os
import json
import csv
import argparse

# Function to find the items within the contents of CSV files in search directories
def find_items_file(item_name):
    for search_dir in search_dirs:
        for file_name in os.listdir(search_dir):
            file_path = os.path.join(search_dir, file_name)
            try:
                with open(file_path, "r") as search_file:
                    file_contents = search_file.read()
                    if item_name in file_contents:
                        break

                        """ with open(item_name, "r") as items_file:
                            csv_reader = csv.reader(items_file)
                            entries = []
                            for i, row in enumerate(csv_reader):
                                if i > 0:  # Skip the first row 
                                    entries.append(row[0])  # Add the first entry on each line to the list"""
                        return entries
            except Exception as e:
                print(f"Error reading file '{file_path}': {e}")
    return [None]

def recurse_into_itemCollection(item_name):
    recursed_matched_entries = {}
    items_file_path = find_items_file(item_name)
    if items_file_path:
        #print(f"Found {item_name} in: {items_file_path}")
        with open(items_file_path, "r") as items_file:
            csv_reader = csv.reader(items_file)
            entries = []
            for i, row in enumerate(csv_reader):
                if i > 0:  # Skip the first row
                    entries.append(row[0])  # Add the first entry on each line to the list
            recursed_matched_entries[item_name] = entries
    else:
        print(f"{item_name} file for '{item_name}' not found in specified directories.")
    return recursed_matched_entries

def actually_recurse_into_itemCollection(item_name):
    '''break down a list of lists into a single list'''
    if not needs_to_recurse(item_name):
        return item_name
    
    #next_item, rest = item_name[0], item_name[1:]
    #if needs_to_recurse(next_item):
    return [actually_recurse_into_itemCollection(next_item) for next_item in find_items_file(item_name)]


def needs_to_recurse(item_name):
    return item_name.startswith("itemCollection")


def process_Faction_Collection(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            item_name = data[0].get("items")
            #print("#####Item Debugging#####\n", item_name)
            return actually_recurse_into_itemCollection(item_name)
            """ if item_name.startswith("itemCollection"):
                matched_entries.update(recurse_into_itemCollection(item_name))
                #print("#####Recursed Entry Debugging#####\n", matched_entries)
            else:
                items_file_path = find_items_file(item_name)
                if items_file_path:
                    #print("#####normal Debugging#####\n")
                    print(f"Found {item_name} in: {items_file_path}")
                    with open(items_file_path, "r") as items_file:
                        csv_reader = csv.reader(items_file)
                        entries = []
                        for i, row in enumerate(csv_reader):
                            if i > 0:  # Skip the first row
                                entries.append(row[0])  # Add the first entry on each line to the list
                        matched_entries[item_name] = entries
                else:
                    print(f"{item_name} file for '{item_name}' not found in specified directories.") """
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {file_path}")
    return None

def process_Faction_Entry(base_dir):
    # Define the two directories to search for the items files relative to base_dir
    all_matched_entries = {}
    # Loop over all files in the base directory
    for file_name in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file_name)
        matched_entries = process_Faction_Collection(file_path)
        """ for item_name, entries in matched_entries.items():
            #print("#####Entry Debugging#####\n", item_name, entries)
            if item_name not in all_matched_entries:
                all_matched_entries[item_name] = []
            all_matched_entries[item_name].extend(entries) """
    #print ("match?",matched_entries)
    return matched_entries

def main():
    parser = argparse.ArgumentParser(description="Process some JSON files.")
    parser.add_argument('base_dir', type=str, help='The base directory containing the JSON files')
    args = parser.parse_args()
    global search_dirs
    search_dirs = [
        os.path.abspath(os.path.join(args.base_dir, "../data")),
        os.path.abspath(os.path.join(args.base_dir, "../StreamingAssets/data/itemCollections/"))
    ]
    matched_entries = process_Faction_Entry(args.base_dir)
    
    print("Matched entries:", matched_entries)
    """get rid of this for now   
    for item_name, entries in matched_entries.items():
        print(f"Processing {item_name} list:")
        for entry in entries:
            print(entry) """

if __name__ == "__main__":
    main()
