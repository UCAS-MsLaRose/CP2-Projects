# Vienna LaRose, Writing to text notes
import csv
"""
r = to read the file
w = write on the file (replaces the old file)
w+ = read and write
a = append (adds to the file, dosen't delete them) (create the file if it dosen't exsist)
x = create a file
a+ = append and read the file
"""
#with open("Notes_6th/test.txt", "a") as file:
#    file.write("randome things and stuff\n")
data = [
    {"username": "jake_waves", "color": "navy"},
    {"username": "mia_flower", "color": "magenta"},
    {"username": "leo_the_great", "color": "brown"},
    {"username": "tina_cakes", "color": "lavender"},
    {"username": "jessica_joy", "color": "gold"},
]
data.pop()
with open("Notes_6th/user_info.csv", "w", newline="") as file:
    fieldnames = ["username" , "color"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open("Notes_6th/user_info.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"username: {row[0]} \ncolor: {row[1]}\n------------------")
