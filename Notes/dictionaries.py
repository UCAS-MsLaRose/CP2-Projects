#Vienna LaRose, Dictionaries Notes
first_car = {
    "make": "Ford",
    "model": "EscapeXLT",
    "year": 2008,
    "color": "Red",
}
current_car = {
    "make": "Mazda",
    "model": "Mazda3",
    "year": 2016,
    "color": "Gray",
}


#print(car["make"][2])

avatar = {
    "earth" : {
        "main_char" :{
            "Toph" : "Best member of Team Avatar. Invented metal bending!"
        },
    },
    "water" : {
        "main_char" :{
            "Katara" : "Team water bender. Team mom. Mastered blood bending",
            "Sokka" : "Team leader. Weilds a boomerang and a sword (later)",
        },
    },
    "fire" : {
        "main_char" :{
            "Zuko" : "Team Lancer. Joins in book 3. Team Firebender. The other favorite character."
        },
    },
    "air" : {
        "main_char" :{
            "Aang" : "Main character. The avatar. Team air bender"
        },
    },
}

#print(avatar["water"]["main_char"])

print(list(first_car.values())[3])
#first_car.pop("color")
print(first_car)
print(first_car.get("make"))
print(first_car.setdefault("color", "white"))
first_car.update({"year": 2025})
print(first_car)
