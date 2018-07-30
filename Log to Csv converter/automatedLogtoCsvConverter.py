# Create a log file into a csv file so we can manipulate it with pandas

import csv
import os


dhcp_path = input("Enter File Path: ")

print("******Please wait while it is converted******")

with open('NewCsvFile.csv', 'w+') as csvfile:
    w = csv.writer(csvfile, dialect='excel')
    with open(dhcp_path) as file:
        lines = file.read().split('\n')
        file = []
        for line in lines:
            file.append(line.split('\t'))
        w.writerows(file)

print("*********** Succesfully converted ***********")

# rename file
renameFile = input('Rename File *add .csv* : ')
os.rename('NewCsvFile.csv', renameFile)

print("Succesfully Renamed: ")
