from pathlib import Path
import csv

def overhead_function():
    '''
    This functions runs everything related to "overheads"
    which includes the return value.
    '''
# create a file to csv file
    fp = Path(r"C:\IGP_PFB_TeamA\csv_reports\overheads-day-52.csv")

# read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        overheads = 0.0 # Creation of needed variables 
        category = ""
        data_to_return = []

        for row in reader: 
            if float(row[1]) > overheads: # If float in row[1] is greater than overhead, it equals overhead
                overheads = float(row[1]) 
                category = row[0] # If float in row [1] is greater than overheads, row[0] would equal to category
        data_to_return.append(f"[HIGHEST OVERHEADS] {category}: {overheads}%") # Take the final output and append it to a list
    return data_to_return
