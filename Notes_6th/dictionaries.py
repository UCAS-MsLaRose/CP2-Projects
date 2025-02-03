# Vienna LaRose, Notes about Dictionaries 
car = {
    "make": "Ford",
    "model": "Escape xlt",
    "year": 2008,
    "color": "Red",
    "name": "Freya"
}

#print(car["make"])

students = {
    "first":{
        1: "Vincent",
        2: "Cecily",
        3: "Evan",
        4: "Sawyer",
        5: "Alishya"
    },
    "sixth": {
        1: "Nicole",
        "color": "Luke",
        3: "Gavin",
        4: "Jackson"
    },
}

#print(students["sixth"]["color"])

#print(list(car.values())[2])

#print(car.get("make"))
#print(students["first"])
#students.pop("first")
#print(students)
#print(car)
#car.popitem()
#print(car)

print(car)
#print(car.setdefault("color", 2))

car.update({"color": "pink"})
print(car)