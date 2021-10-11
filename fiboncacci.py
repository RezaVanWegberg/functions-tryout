Getal0 = 1
Getal1 = 1
Getal2 = 0
a = 1
def fibonacci(a):
    global Getal0
    global Getal1
    global Getal2
    while Getal2 < 10000 :        
        Getal2 = Getal0 + Getal1
        print(Getal2)
        Getal0 = Getal1
        Getal1 = Getal2
    return(fibonacci)
fibonacci(1)