from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        return f"{self.values[self.value]} of {self.suits[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = [Card(v, s) for v in range(2, 15) for s in range(4)]
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def reshuffle(self):
        self.__init__()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("Player 1 name: ")
        name2 = input("Player 2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.rounds = 0

    def wins(self, winner):
        print(f"{winner} wins this round!")

    def draw(self, p1n, p1c, p2n, p2c):
        print(f"{p1n} drew {p1c}, {p2n} drew {p2c}")

    def display_score(self):
        print(f"Score: {self.p1.name} ({self.p1.wins}) - {self.p2.name} ({self.p2.wins})")

    def play_game(self):
        print("Beginning War!")
        while len(self.deck.cards) >= 2:
            self.rounds += 1
            response = input("Press Enter to play, 'q' to quit: ")
            if response.lower() == 'q':
                break

            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            if not p1c or not p2c:
                self.deck.reshuffle()
                continue

            self.draw(self.p1.name, p1c, self.p2.name, p2c)

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            elif p1c < p2c:
                self.p2.wins += 1
                self.wins(self.p2.name)
            else:
                print("It's a tie! Drawing one more card each.")
                self.play_tiebreaker()

            self.display_score()

        win = self.winner(self.p1, self.p2)
        print(f"War is over after {self.rounds} rounds. {win} wins!")

    def play_tiebreaker(self):
        p1c = self.deck.rm_card()
        p2c = self.deck.rm_card()
        if not p1c or not p2c:
            self.deck.reshuffle()
            return
        print(f"Tiebreaker - {self.p1.name} drew {p1c}, {self.p2.name} drew {p2c}")
        if p1c > p2c:
            self.p1.wins += 1
            self.wins(self.p1.name)
        else:
            self.p2.wins += 1
            self.wins(self.p2.name)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It's a tie!"


if __name__ == '__main__':
    game = Game()
    game.play_game()
      
