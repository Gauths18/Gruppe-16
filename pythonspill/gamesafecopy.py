import random


navn = input("navn brah: ")
intro = False
roomtypes = ["treasure", "monster", "trap", "restingpoint", "puzzle"]
hp = 100




print("Velkommen til spillet, " + navn + "!")
print("Du har " + str(hp) + " hp.")
def treasure_room():
    print("Du har kommet til et skattkammer! Du finner en skatt og får 20 hp.")
    global hp
    hp += 20
def monster_room():
    print("Du har kommet til et monsterrom! Du møter et monster og mister 30 hp.")
    global hp
    hp -= 30
def trap_room():
    print("Du har kommet til et fellerom! Du utløser en felle og mister 20 hp.")
    global hp
    hp -= 20
def restingpoint_room():
    print("Du har kommet til et hvilested! Du hviler og får 10 hp.")
    global hp
    hp += 10
def puzzle_room():
    print("Du har kommet til et puslerom! Du løser en gåte og får 15 hp.")
    global hp
    hp += 15
def encounter_room(roomtype):
    if roomtype == "treasure":
        treasure_room()
    elif roomtype == "monster":
        monster_room()
    elif roomtype == "trap":
        trap_room()
    elif roomtype == "restingpoint":
        restingpoint_room()
    elif roomtype == "puzzle":
        puzzle_room()


def choose_room():
    roomtype1 = random.choice(roomtypes)
    roomtype2 = random.choice(roomtypes)
    print("Du har kommet til et rom. Det er to dører foran deg.")
    print("Dør 1: " + roomtype1)
    print("Dør 2: " + roomtype2)
    valg = input("Velg en dør (1 eller 2): ")
    if valg == "1":
        print(f"Du velger dør 1 og møter et {roomtype1} rom.")
        encounter_room(roomtype1)
    elif valg == "2":
        print(f"Du velger dør 2 og møter et {roomtype2} rom.")
        encounter_room(roomtype2)
    else:
        print("Ugyldig valg.")

while hp > 0:
    print("Du har " + str(hp) + " hp.")
    if not intro:
        print("Du ankommer fangehullet. går du videre? (ja/nei)")
        intro = True
    choice = input()
    if choice == "ja":
        print("Du går videre.")
        choose_room()
    elif choice == "nei":
        print("Du velger å ikke gå videre. Spillet avsluttes.")
        break
    else:
        print("Ugyldig valg. Vennligst velg 'ja' eller 'nei'.")




