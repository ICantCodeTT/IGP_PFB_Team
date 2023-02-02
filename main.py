import profit_loss, cash_on_hand, overheads
from pathlib import Path

# Assigns the file path for summary_report.txt to the variable text so that the code can write to this file later
text = Path(r"C:\IGP_PFB_TeamA\summary_report.txt")  


def write_file(files):
    '''
    This function takes the files and its individual output
    and write into a txt file
    '''
    # Open the file specified by the text variable in write mode and assigns it to variable f
    with open(text, 'w') as f:
        for file in files: # Take the individual file in files (eg.profit, cash, overhead)
            for data in file: # Take the individual data in file (eg. 1st and 2nd output of profit)
                f.write(f"{data}\n") # Write the data into txt file, newline after each.

def main():
    '''
    This functions coordinates all the other 3 py files 
    as well as their return values. 
    '''
    profit = profit_loss.profitloss_function() # Variables to store all the output of the 3 functions
    cash = cash_on_hand.coh_function()
    overhead = overheads.overhead_function()
    write_file([profit, cash, overhead]) # Calling of the write functions to write the 3 files into a txt file
  
main()
