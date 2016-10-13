import csv


# read the training data
train_file = open("example1.csv", newline='', encoding="utf-8")
reader = csv.reader(train_file)

train_list = []
for row in reader:
    train_list.append(row)
    print(row)


