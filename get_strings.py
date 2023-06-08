# This file is used to extract ASCII strings from PE file
import csv
import subprocess
import os

folder_path = "/home/kali/Downloads/Dataset/"

# open the input and output CSV files
for file_name in os.listdir(folder_path):
    if file_name == "Benign.csv" or file_name == "Malware.csv":
        file_path = os.path.join(folder_path, file_name)
        out_path = os.path.join(folder_path, file_name[:-4])
        print("Output file: " + out_path)
        
        # open the input and output CSV file
        with open(file_path, 'r') as input_file, open(out_path, 'w', newline='') as output_file:
            # create CSV reader object
            reader = csv.reader(input_file)
            next(reader, None) # skip the header
            
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
                decoded_output = strings_output.decode('ascii', errors='replace') # replace with (?) if encounter errors
                
                # create a list of strings from decoded output that are not empty/only whitespace
                extracted_strings = [s.strip() for s in decoded_output.split('\n') if len(s.strip()) > 0]
                
                # write the extracted strings to the text file: 1 row contains list of strings extracted from a file
                for string in extracted_strings:
                    output_file.write(string + " ")
                output_file.write("\n")