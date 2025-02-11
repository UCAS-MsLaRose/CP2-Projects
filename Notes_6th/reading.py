# Vienna LaRose, Reading Notes Python
import csv

with open("Notes_6th/test.txt", "r") as file:
    content = file.read()
    #print(content[5:20].upper())

file = open("Notes_6th/test.txt", "r").read()

users = {}

with open("Notes_6th/user_info.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        users.update({row[0]:row[1]})

print(users)