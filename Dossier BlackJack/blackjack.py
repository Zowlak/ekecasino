import random
import timeit

enseigne=["♠", "♥", "♣ ", "♦ "]
valeur=[2, 3, 4, 5, 6, 7, 8, 9, 10, "VALET", "DAME", "ROI", "AS"]
def creation():
    return [(x,y) for x in valeur for y in enseigne]

paquet = creation()
for i in range(500):
    random.shuffle(paquet)

print(paquet)

class Jeu:
    def __init__(self):
        pass
    
print(timeit.timeit(creation))
