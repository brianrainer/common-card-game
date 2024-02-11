# spade, heart, club, diamond
CARD_SUITS = ['\u2660', '\u2665', '\u2663', '\u2666']


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} {self.suit}"

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit


def main():
    deck = []

    for suit in CARD_SUITS:
        for value in range(1, 14):
            deck.append(Card(value, suit))

    for card in deck:
        print(card)


main()