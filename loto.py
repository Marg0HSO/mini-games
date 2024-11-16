import random as r

def setPlayerNumbers()->list:
    playerNumbers = []
    for i in range(5):
        n = int(input("Nombre choisi (entre 1 et 99) --> "))
        while n > 99 or n <= 0:
            print("un nombre entre 1 et 99 seulement")
            n = int(input("Nombre choisi (entre 1 et 99) --> "))  
        playerNumbers.append(n)
    starNumber = int(input("L'étoile entre 1 et 9 --> "))
    while starNumber > 9 or starNumber < 1:
        starNumber = int(input("L'étoile entre 1 et 9 --> "))
    playerNumbers.append(starNumber)
    return playerNumbers

def pullNumbers()->list:
    numbers = [r.randint(1, 99) for i in range(5)]
    starNumber = r.randint(1, 9)
    numbers.append(starNumber)
    assert len(numbers) == 6, "Erreur de tirage"
    return numbers

def mainloop():
    PlayerNumbers = setPlayerNumbers()
    print(f"Chiffres du joueur --> {PlayerNumbers}")
    # numbers = pullNumbers()
    numbers = [10, 20, 30, 40, 50, 9]
    print(f"Le tirage est --> {numbers}")
    if numbers == PlayerNumbers:
        print("NOTRE GRAND GAGNANT !!")
    else:
        print("Dommage ça sera pas pour cette fois")

mainloop()