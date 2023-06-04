# not done, still in process
import csv

input_csv = "/home/kali/Downloads/Dataset/"

with open(input_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Iterate over the rows of the CSV file.
    for row in reader:

        # Create a list of words.
        words = []

        # Iterate over the columns of the row.
        for column in row:

            # Split the column into words.
            words.extend(column.split())
