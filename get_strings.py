# This file is used to extract ASCII strings from PE file
import csv
import subprocess
import os

csv_path = "/home/kali/Downloads/NT230.N22.ATCL-Group5/folder_info.csv"
out_path = "/home/kali/Downloads/NT230.N22.ATCL-Group5/string_of_pe.csv"

# open the input and output CSV files
with open(csv_path, 'r') as input_file, open(out_path, 'w', newline='') as output_file:
    # create CSV reader and writer objects
    reader = csv.reader(input_file)
    next(reader, None) # skip the header
    writer = csv.writer(output_file)
    
    # iterate over each row in the input CSV file
    for row in reader:
        # extract the filename from the first column of the row
        filepath = row[0]
        # get file name from file path
        filename = os.path.basename(filepath)
        print(filename + "\n")
        # run the strings command on the file and capture its output
        strings_output = subprocess.check_output(['strings', filepath])
        
        # process the output to extract the strings
        decoded_output = strings_output.decode('ascii', errors='replace') # replace if encounter errors
        extracted_strings = [s.strip() for s in decoded_output.split('\n') if len(s.strip()) > 0]

        # write the extracted strings to the strings_of_pe.csv file: 1 row contains strings of a file
        writer.writerow(extracted_strings)