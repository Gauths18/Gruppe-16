import random


navn = input("navn brah: ")
intro = False
roomtypes = ["treasure", "monster", "trap", "restingpoint", "puzzle"]
hp = 100


print("Velkommen til spillet, " + navn + "!")
print("Du har " + str(hp) + " hp.")

def choose_room():
    roomtype1 = random.choice(roomtypes)
    roomtype2 = random.choice(roomtypes)
    print("Du har kommet til et rom. Det er to dører foran deg.")
    print("Dør 1: " + roomtype1)
    print("Dør 2: " + roomtype2)
    valg = input("Velg en dør (1 eller 2): ")
    if valg == "1":
        print(f"Du velger dør 1 og møter et {roomtype1} rom.")
    elif valg == "2":
        print(f"Du velger dør 2 og møter et {roomtype2} rom.")
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




