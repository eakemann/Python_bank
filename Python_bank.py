# import cs reader
import csv
# import os
import os
#open csv
filepath = os.path.join("budget_data.csv")
with open(filepath) as budget_data:
    read_csv = csv.reader(budget_data, delimiter=',')
     # Read the header
    header = next(read_csv)
    print(f'The headers are: {header}')
    # Total number of months
    sum_of_months = sum(1 for row in read_csv)
    print(f"Total Months: {sum_of_months}")

        
# Calculate Profit or Loss



       


