# importing Path and csv
from pathlib import Path
import csv

# file path for day 51's overheads data
file_path = Path.cwd()/"csv_reports"/"overheads-day-51.csv"

# open day 51's overhead data to read it
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    # reading the csv file
    reader = csv.reader(file)
    # skipping the header
    next(reader)

    # creating an empty list to store the overhead data
    overhead_data = []

    # creating a for loop for the rows in reader
    for row in reader:
        # converting the overhead values into float
        # appending both overhead values (in row 1) and overhead category (in row 0) into the empty list created
        overhead_data.append([float(row[1]),row[0]])

# file path for summary report
file_path = Path.cwd()/"summary_report.txt"

def overhead_function():
    """
    - This function arranges the overhead data from the highest to the lowest
    - After arrangement, this function writes the highest overhead value in the summary report
    """
    # open summary report to write overheads data into it
    with file_path.open(mode="w", encoding="UTF-8", newline="") as file:
        # sorting the overhead data from highest to lowest
        overhead_data.sort(reverse=True)
        # writing the highest overheads category and value in the summary report
        file.write(f"[HIGHEST OVERHEADS] {overhead_data[0][1].upper()}: {overhead_data[0][0]}%")