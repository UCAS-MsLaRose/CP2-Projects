import csv
data = [
    {"username": "jake_waves", "color": "navy"},
    {"username": "mia_flower", "color": "magenta"}, 
    {"username": "leo_the_great", "color": "brown"}, 
    {"username": "tina_cakes", "color": "lavender"},
    {"username": "jessica_joy", "color": "gold"}
]

items = [
    ["jake_waves", "navy"],
    ["mia_flower", "magenta"],
    ["leo_the_great", "brown"],
    ["tina_cakes", "lavender"],
    ["jessica_joy", "gold"]
]

with open('Notes_2nd\sample.csv', 'w', newline='') as file:
    fieldnames = ["username", "color"]
    writer = csv.writer(file, delimiter="|")
    writer.writerows(items)

with open('Notes_2nd\sample.csv', 'r',) as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        print({row[0]:row[1]})