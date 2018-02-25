#!/usr/bin/python2

import csv 
import string

fname = "1228136.csv"

reader = ""
with open(fname, "r") as f:
    next(f)
    reader = csv.reader(f)

    hourlyData = []
    avgData = []
    fields = [5, 7, 8, 10, 16, 17, 19, 20]
    avgFields = [28, 30, 44, 42]
    for row in reader:
        for field in fields:
            if field == 5 or field == 7:
                hourlyData.append(row[field])
            elif field == 8 or field == 20:
                if not row[field][-1:].isdigit():
                    row[field] = row[field][:-1]
                row[field] = float(row[field] if row[field] else 0.0)
                hourlyData.append(row[field])
            else:
                if not row[field][-1:].isdigit():
                    row[field] = row[field][:-1]
                row[field] = int(row[field] if row[field] else 0)
                hourlyData.append(row[field])
        print(hourlyData) 

        for avgField in avgFields:
            if avgField == 41:
                if not row[avgField][-1:].isdigit():
                    row[avgField] = row[avgField][:-1]
                row[avgField] = float(row[avgField] if row[avgField] else 0.0)
                avgData.append(row[avgField])
            else:
                if not row[avgField][-1:].isdigit():
                    row[avgField] = row[avgField][:-1]
                row[avgField] = int(row[avgField] if row[avgField] else 0)
                avgData.append(row[avgField])
        print(avgData)
