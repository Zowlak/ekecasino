import blackjackDealer as Bjd


class Player(Bjd.Dealer):
    """Ceci est la classe du joueur. Ses actions sont listés en dessous."""
    def __init__(self, name, funds, bet=0):
        """Définition des variables"""
        super().__init__()
        self.name = name
        self.funds = funds
        self.bet = bet

    def place_bet(self, amount=10):
        """Appelé à chaque tour, il montre combien on a dans notre banque et notre mise"""
        self.funds -= amount
        self.bet += amount

    def payout(self):
        """Le joueur gagne l'équivalent de sa mise en plus de reprendre sa mise initiale"""
        self.funds += (self.bet * 2)
        self.bet = 0

    @staticmethod  # Permet d'appeler la fonction n'importe quand.
    def hit_or_stick():
        """La fonction qui demande le joueur s'il veut tirer une nouvelle carte ou pas. A vous de voir"""
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
