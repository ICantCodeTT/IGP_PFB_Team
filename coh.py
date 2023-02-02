from pathlib import Path
import csv

def coh_function():
    '''
    This functions runs everything related to "cash on hand"
    which includes the return value.
    '''
# create a file to csv file
    fp = Path(r"C:\IGP_PFB_TeamA\csv_reports\cash-on-hand-usd (Day 48 to 52).csv")

# read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header


        cashonhand = 0 # Creation of needed variables
        row_counter = 0
        check = 0
        data_to_return = []