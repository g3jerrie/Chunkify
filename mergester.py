# 
#   Chunkify
#
#   @g3jerrie
#



import os
import re
import shutil

def get_number (file):
    #Use a regular expression to find the number in the file name
    match = re.search ('(\d+)', file)
    if match:
        # Return the number as integer
        return int (match.group (1))
    else:
        # Return a large number if no number is found
        return 999999

def merge_files(directory, pattern, merged_file):
    # Get the list of files that match the pattern
    files = [f for f in os.listdir(directory) if f.startswith(pattern)]
    # Sort the files by the file names
    files.sort (key=get_number) #Python is lexicographical
    # Print the file list and the number of files
    print(f"There are {len(files)} files to be merged:")
    print(*files, sep="\n")
    # open the merged file in write mode
    with open(merged_file, 'wb') as outfile:
        # Loop through the files and copy their contents to merged file
        for file in files:
            file_path = os.path.join(directory, file)
            with open(file_path, 'rb') as infile:
                shutil.copyfileobj(infile, outfile)
                
directory = '.'
pattern = 'chunk_'
merged_file = 'largeFileName.zip'

merge_files(directory, pattern, merged_file)