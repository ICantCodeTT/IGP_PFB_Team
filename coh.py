from pathlib import Path
import csv

def coh_function():
    '''
    This function computes every value related to "cash on hand"
    Including the return value.
    '''
# Create a file to csv file
    fp = Path(r"C:\IGP_PFB_TeamA\csv_reports\cash-on-hand-usd (Day 48 to 52).csv")

# Read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        
        # Skip header
        next(reader) 
        
        # Create empty list to store calculated values
        cashonhand = 0 
        row_counter = 0
        check = 0
        data_to_return = []
     for row in reader:
            row_counter += 1
            
            # If int in row[1] is greater than cash on hand, it equals to cash on hand
            if int(row[1]) > cashonhand: 
                cashonhand = int(row[1])
                
                # Check by counting if all the rows is greater than cash on hand
                check += 1 
            else: 
                # Append all the days that are lower than the previous days
                data_to_return.append(f"[CASH DEFECIT] DAY: {row[0]}, AMOUNT: USD{cashonhand - int(row[1])}")
                cashonhand = int(row[1])
                
        # "CASH SURPLUS" statement will be appended if check and row_counter have the exact final value
        if check == row_counter:
            data_to_return.append(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    return data_to_return
