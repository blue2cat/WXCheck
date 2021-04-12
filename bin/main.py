#programatic analisis 

# python imports
import csv

#wxcheck imports
#from db_connect import *


import csv
total = int(0)
c = int(0)
with open('2540765.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        row_date = row[5][5:]
        if row_date == '04-11':
            if row[18] != "":
                temp = int(row[18])
                c = c + 1
                print(row[5])
                print(row[18])
                total = total + temp


print(total/c)

