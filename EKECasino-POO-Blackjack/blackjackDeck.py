from random import shuffle
from time import sleep


class Deck:
    """Cette classe créé le paquet de cartes à chaque partie."""
    def __init__(self):
        """On définit les cartes"""
        self.stack = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
                      ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
                      ('J', 10), ('Q', 10), ('K', 10)] * 4
        print("Nous mélangeons les cartes, veuillez patienter")
        self.shuffle()

    def shuffle(self):
        """On mélange. 500 fois car on ne sait jamais."""
        sleep(2)
        for _ in range(500):
            shuffle(self.stack)

    def deal_card(self):
        """On retire l'élément tiré du tableau."""
        return self.stack.pop()
