
import csv
import urllib.request

filename = "playtennis.csv"
csvfile = open(filename, newline='', encoding="utf-8")
wordReader = csv.reader(csvfile)
# each row is a list of string now

# read the file and split into list

totalList = []
for row in wordReader:
    line = []
    line.append(row)
    totalList.append(line)

numOfInst = len(totalList)
numOfAttr = len(totalList[1])

print(numOfAttr)
print(numOfInst)

