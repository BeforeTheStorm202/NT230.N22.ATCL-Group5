import csv
import subprocess
import os

csv_path = "/home/kali/Downloads/MalwareProject/folder_info.csv"
out_path = "/home/kali/Downloads/MalwareProject/strings_of_pe.csv"
out_pathv2 = "/home/kali/Downloads/MalwareProject/strings_of_pe_v2.csv"

# open the input and output CSV files
with open(csv_path, 'r') as input_file, open(out_pathv2, 'w', newline='') as output_file:
    # create CSV reader and writer objects
    reader = csv.reader(input_file)
    next(reader, None) # skip the header
    writer = csv.writer(output_file)
    
    # iterate over each row in the input CSV file
    for row in reader:
        # extract the filename from the first column of the row
        filename = row[0]
        #filename = os.path.basename(filepath)
        print(filename + "\n")
        # run the strings command on the file and capture its output
        strings_output = subprocess.check_output(['strings', filename])
        
        # process the output to extract the strings
        decoded_output = strings_output.decode('ascii', errors='replace')
        extracted_strings = [s.strip() for s in decoded_output.split('\n') if len(s.strip()) > 0]

        for string in extracted_strings:
            # write the extracted string to the strings_of_pe_v2.csv file: 1 row contains 1 string
            writer.writerow(string)

        # write the extracted strings to the strings_of_pe.csv file: 1 row contains strings of a file
        # writer.writerow(extracted_strings)
