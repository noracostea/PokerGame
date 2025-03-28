from deck import Deck, Card

class Hand:
    def __init__(self, deck):
        cards = []
        for i in range(5):
            cards.append(deck.deal_card())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    @property
    def is_flush(self):
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is pair(self):
        matches = 0
        for c1 in self.cards:
            for c2 in self.cards:
                if c1 == c2:
                    continue
        for i in range(5):
            for j in range (5:
                if i == j:
                    continue:
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        if matches == 2:
            return True
        return False

matches = 0
count = 0
while matches < 10000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_pair:
        print(hand)
        matches += 1
        #break

print(f"The probability of a flush is {100*matches/count}")