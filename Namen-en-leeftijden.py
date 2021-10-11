def HalloNaam():
    print("Hallo", Naam, ", je leeftijd is", Getal, "jaar")

loop = True
while loop:
    Naam = input("Wat is uw naam? :")
    Getal = int(input("Hoe oud bent u? :"))
    HalloNaam()
    Herhaling = input("Als u wilt stoppen, typ dan 'stop'. Als u door wilt gaan typ dan 'opnieuw'. :")
    if Herhaling == "stop":
        loop = False
    else:
        loop = True

