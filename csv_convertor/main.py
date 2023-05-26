import json
import csv

# Opening JSON file and loading the data
# into the variable data
with open("E:\Downloads\data.json") as json_file:
    data = json.load(json_file)

employee_data = data['Issues_History']

# now we will open a file for writing
data_file = open(r'E:\Downloads\data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for emp in employee_data:
    if count == 0:
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(emp.values())

data_file.close()

# importing pandas module
import pandas as pd
import openpyxl
# reading the csv file
cvsDataframe = pd.read_csv(r'E:\Downloads\data_file.csv')
print("file converted")

resultExcelFile = pd.ExcelWriter('ResultExcelFile.xlsx')
print("file created")
cvsDataframe.to_excel(resultExcelFile, index=False)
resultExcelFile.save()