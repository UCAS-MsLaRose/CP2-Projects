# Vienna LaRose, Reading files notes
import csv
users = {}
content = open('Notes_2nd/things.txt', 'r').read()
#print(int(content)+6)

with open("Notes_2nd/sample.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        users.update({row[0]:row[1]})

print(users)

