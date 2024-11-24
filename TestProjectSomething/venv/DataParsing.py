import csv
import os

def ParseData(filename):
    with open(filename, 'r') as file:
        spamreader = csv.reader(file)
        data = list(spamreader)
        print(data)

ParseData("E:/The Rota Scheduler/ViewEmployeesOnRota.xls.csv")
