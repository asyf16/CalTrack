import csv

def getdata():
    dict1={}
    foodnames = []
    foodcals = []
    names = open("Images/data.csv", 'r',encoding='utf-8-sig')
    reader = csv.reader(names)
    for row in reader:
        if row:  # Check if the row is not empty
            dict2={row[0]:int(row[1])}
            dict1.update(dict2)
    return dict1
