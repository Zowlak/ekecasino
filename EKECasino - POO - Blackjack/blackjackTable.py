from random import shuffle
from colorama import Fore, Style
from time import sleep
import blackjackDealer as Bjd


class Table(object):

    def __init__(self, player, funds=100):

        self.dealer = Bjd.Dealer()
        self.player = Player(player, funds)
        self.deck = Deck()

        # call table_setup() method to shuffle and deal first cards
        self.table_setup()

    def table_setup(self):

        # Mélange les cartes
        self.deck.shuffle()

        # On met la mise
        self.player.place_bet()

        # Distribue les cartes
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.calculate_score(self.player)  # Calcul du score pour voir s'il y a blackjack ou pas
        self.calculate_score(self.dealer)

        self.main()

    def main(self):

        while True:
            print()
            print(self)
            player_move = self.player.hit_or_stick()
            if player_move is True:
                self.deal_card(self.player)
                self.calculate_score(self.player)
            elif player_move is False:
                self.dealer_hit()

    def dealer_hit(self):

        score = self.dealer.score
        while True:
            if score < 17:
                self.deal_card(self.dealer)
                self.calculate_score(self.dealer)
                print(self)
            else:
                self.check_final_score()

    def __str__(self):  # Affiche les scores actuels

        dealer_hand = [card for card, value in self.dealer.hand]
        player_hand = [card for card, value in self.player.hand]

        print(Fore.YELLOW + "Main du Dealer : {}".format(dealer_hand))
        print("Score du Dealer : {}".format(self.dealer.score))
        print()
        print(Fore.BLUE + "Main de {} : {}".format(self.player.name, player_hand))
        print("Score de {} : {}".format(self.player.name, self.player.score))
        print()
        print(("Mise de {} : {}.".format(self.player.name, self.player.bet)))
        print("Argent de {} : {}.".format(self.player.name, self.player.funds))
        print(Style.RESET_ALL + "~" * 40)
        return ''

    def deal_card(self, player):

        card = self.deck.stack.pop()
        player.hand.append(card)

    def calculate_score(self, player):

        ace = False  # Cherche si AS
        score = 0
        for card in player.hand:
            if card[1] == 1 and not ace:
                ace = True
                card = ('A', 11)
            score += card[1]
        player.score = score
        if player.score > 21 and ace:
            player.score -= 10
            score = player.score
        self.check_win(score, player)
        return

    def check_win(self, score, player):
        if score > 21:
            print()
            print(self)
            print(Fore.RED + "{} dépasse".format(player.name))
            print(Style.RESET_ALL)
            self.end_game()
        elif score == 21:
            print(self)
            print(Fore.GREEN + "{} blackjack !".format(player.name))
            print(Style.RESET_ALL)
            try:
                player.payout()
            except:
                pass
            self.end_game()
        else:
            return

    def check_final_score(self):

        dealer_score = self.dealer.score
        player_score = self.player.score

        if dealer_score > player_score:
            print("Le Dealer a gagné!")
        else:
            print("{} a gagné !".format(self.player.name))
        self.end_game()

    def end_game(self):

        bank = self.player.funds
        if bank >= 10:
            again = input("Voulez-vous rejouer (O/N)? ")
            if again.lower().startswith('o'):
                print(chr(27) + "[2J")
                self.__init__(self.player.name, funds=self.player.funds)
            elif again.lower().startswith('n'):
                exit(1)
        else:
            print("Vous n'avez plus d'argent, n'hésitez pas à revenir avec plus de chance !")
            # exit(2)


class Player(Bjd.Dealer):

    def __init__(self, name, funds, bet=0):
        super().__init__()
        self.name = name
        self.funds = funds
        self.bet = bet

    def place_bet(self, amount=10):

        # Appelé à chaque tour, il montre combien on a dans notre banque et notre mise
        self.funds -= amount
        self.bet += amount

    def payout(self):

        # Le joueur gagne l'équivalent de sa mise en plus de reprendre sa mise initiale
        self.funds += (self.bet * 2)
        self.bet = 0

    @staticmethod
    def hit_or_stick():
        while True:
            choice = input("Voulez-vous une autre carte (O/N)? ")
            if choice.lower().startswith('o'):
                print(chr(27) + "[2J")
                return True
            elif choice.lower().startswith('n'):
                print(chr(27) + "[2J")
                return False
            else:
                print("Je n'ai pas compris, veuillez répéter pour le sourd s'il vous plaît")
                continue


class Deck(object):

    def __init__(self):
        self.stack = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
                      ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
                      ('J', 10), ('Q', 10), ('K', 10)] * 4
        print("Nous mélangeons les cartes, veuillez patienter")
        self.shuffle()

    def shuffle(self):
        sleep(2)
        for _ in range(500):
            shuffle(self.stack)

    def deal_card(self):
        return self.stack.pop()


def main():
    player_name = input("Bienvenue à l'EKECasino, puis-je demander votre nom ? ")
    print("Bonne chance {}, que la chance soit de votre côté. Voici votre table.".format(player_name))
    Table(player_name)


main()