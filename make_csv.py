import os
import csv
import datetime

dir_path = "/home/kali/Downloads/MalwareProject/"
csv_path = "/home/kali/Downloads/MalwareProject/folder_info.csv"

# List all files in the folder and their info
files_info = []

# Loop through all folders in specified directory
for folder_name in os.listdir(dir_path):
    folder_path = os.path.join(dir_path, folder_name)
    print(folder_path + "\n")
    # Check if item in directory is a folder
    if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):  # Only consider files (not subfolders, etc.)
                    mod_time = os.path.getmtime(file_path)  # Get modification time in seconds since epoch
                    mod_date = str(datetime.date.fromtimestamp(mod_time))  # Convert to readable datetime format
                    if "Benign" in folder_path:
                        label = 0
                    else:
                        label = 1
                    files_info.append([file_path, label, mod_date])

# Write files_info to CSV file
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Path", "Label", "Date"])  # Header row
    for file_info in files_info:
        writer.writerow(file_info)