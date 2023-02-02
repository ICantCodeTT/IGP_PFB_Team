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
        # skip header
        next(reader) 
        
        # Creation of needed variables
        cashonhand = 0 
        row_counter = 0
        check = 0
        data_to_return = []
     for row in reader:
            row_counter += 1
            # If int in row[1] is greater than cashonhand, it equals to cashonhand
            if int(row[1]) > cashonhand: 
                cashonhand = int(row[1])
                # check by counting if all the rows is greater than cashonhand
                check += 1 
            else: 
                # Append all the days that are lower than the previous days
                data_to_return.append(f"[CASH DEFECIT] DAY: {row[0]}, AMOUNT: USD{cashonhand - int(row[1])}")
                cashonhand = int(row[1])
        # Only if check and row_counter have the exact final value, it will append "CASH SURPLUS" statement
        if check == row_counter:
            data_to_return.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    return data_to_return
