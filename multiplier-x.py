getal = int(input("Van welk getal wilt u de tafel zien? "))
a = 1
def tafel():
    for x in range(10):
        global a
        print(getal*a)
        a += 1

tafel()
