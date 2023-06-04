# This file is used to create the list of file names and assign their labels in both cleanware & malware folder
import os
import csv
import datetime

dir_path = "/home/kali/Downloads/MalwareProject/"
csv_path = "/home/kali/Downloads/Dataset/"

def write_to_csv(folder_name, files_info):
    out_path = os.path.join(csv_path, folder_name)
    # Write files_info to CSV file
    with open(out_path + ".csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File Name", "Label"])  # Header row
        for file_info in files_info:
            writer.writerow(file_info)

# Loop through all folders in specified directory
for folder_name in os.listdir(dir_path):
    # List all files in the folder and their info
    files_info = []

    folder_path = os.path.join(dir_path, folder_name)
    print(folder_path + "\n")
    
    # Check if item in directory is a folder
    if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):  # Only consider files (not subfolders, etc.)
                    if "Benign" in folder_path:
                        label = 0 # Cleanware
                    else:
                        label = 1 # Malware
                    files_info.append([file_path, label])
    write_to_csv(folder_name, files_info)