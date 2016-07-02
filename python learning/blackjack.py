import random
class Card:
  def __init__(self, suit, face, value):
    self.suit = suit
    self.face = face
    self.value = value

def __str__(self):
    return "{f} of {s}".format(f=self.face, s=self.suit)
def __reper__(self):
    return "{f} of {s}".format(f=self.face, s=self.suit)

class Deck:
    def __init__(self):
     self.cards = self.create_deck()
     self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def create_deck(self):
        deck = []
        suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
        face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King"]
        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for s in suit:
            x = 0
            for f in face:
                card = Card(s, f, value[x])
                deck.append(card)
                x += 1
        return deck

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.create_players()

    def create_players(self):
        pl_num = int(input("How many players are there?"))
        for pl in range(1, pl_num + 1):
            player = Hand(input("Player {num}, what is your name?".format(num = pl)))
            self.players.append(player)

    def deal(self):
        for pl in self.players:
            c1 = self.deck.cards.pop()
            c2 = self.deck.cards.pop()
            pl.cards.append(c1)
            pl.cards.append(c2)

    def hit(self):
        card = self.deck.cards.pop()
        return card

    def run_game(self):
        print("Welcome to BlackJack")
        self.deal()
        for pl in self.players:
                print("**********")
                pl.get_score()
                print(pl.name)
                print(pl.hand_value)
                print("**********")

        for pl in self.players:
            pl_turn = True
            while pl_turn:
                pl.get_score()
                if pl.hand_value == 21:
                    print("BlackJack! You win this hand {}!".format(pl.name))
                    pl_turn = False
                    continue
                elif pl.hand_value > 21:
                    print("You bust {}".format(pl.name))
                    pl_turn = False
                    continue
                print("{}, your hand consists of {} and {}".format(pl.name, pl.cards
                [:-1], pl.cards[-1]))
                choice = input("Do you wish to hit or stay: ").lower()
            if choice == "hit":
                pl.cards.append(self.hit())
                pl.get_score()
                print(pl.name)
                print(pl.hand_value)

            elif choice == "stay":
                pl_turn = False
                pl.get_score()
                print(pl.name)
                print(pl.hand_value)
            else:
                print("I don't Understand that...")

            else:
                self.dealer.get_score()
                dealer_turn = True
                while dealer_turn:
                    self.dealer.get_score()
                    print("dealer shows {}. {} total points".format
                    (self.dealer.cards, self.dealer.hand_value))
                    if self.dealer.hand_value <  17
                        self.dealer.cards.append(self.hit())
                else:
                    dealer_turn = False

            else:
                for pl in self.players:
                    if pl.hand_value > self.dealer.hand_value:
                        print("You win {}!".format(pl.name))
                    elif pl.hand_value == self.dealer.hand_value:
                        print("You push {}.".format(pl.name))
                    else:
                        print("You lose {}!".format(pl.name))
class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.hand_value = 0

    def get_score(self):
        self.hand_value = 0
        number_of_aces = 0
        for card in self.cards:
            if card.face == "Ace":
                number_of_aces += 1
            else:
                self.hand_value += card.value
        if number_of_aces > 0:
            for aces in range(number_of_aces):
                self.hand_value += 1
            else:
                if self.hand_value + 10 <= 21:
                    self.hand_value += 10

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

game = BlackJack()
game.run_game()
# print(game.players)
