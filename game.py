from deck import Deck, Card

class Hand:
    def __init__(self,deck):
        """
        Method that creates and deals a 5 card hand
        :param deck: the poker deck
        """
        cards=[]
        for i in range(5):
            cards.append(deck.deal())
        self._cards=cards

    @property
    def cards(self):
        """
        Decorator method to access the cards as .cards and not as ._cards
        :return: cards
        """
        return self._cards

    def __str__(self):
        """
        Magic method on how to print the deck as a string
        :return: list of cards in the deck as a string
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Method that checks if a hand is a flush or not by comparing all the cards in the hand with the first
        :return: True if it is a flush and False if it is not a flush
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Goes over each hand and returns the amount of matches
        :return: number of matches
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks if a hand has 1 pair
        :return: TRUE if it has 1 pair, FALSE if it doesn't have 1 pair
        """
        if self.num_matches==2: #One pair is 2 matches
            return True
        return False

    @property
    def is_2pair(self):
        """
        Checks if a hand has 2 pairs
        :return: TRUE if it has 2 pairs, FALSE if it doesn't have 2 pairs
        """
        if self.num_matches == 4:  # One pair is 2 matches
            return True
        return False

    @property
    def is_trips(self):
        """
        Checks if a hand has 3 pairs
        :return: True if it does/ False if it doesn't
        """
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        """
        Checks if a hand has 6 pairs
        :return: True if it does/ False if it doesn't
        """
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        """
        Checks if a hand is a full house, if it has 8 matches
        :return: TRUE if full house, FALSE if else
        """
        if self.num_matches == 8:
            return True
        else:
            return False

    @property
    def is_straight(self):
        """
        Checks if a hand is a straight by checking if:
        1. There are no repeated cards, the number of matches is 0
        2. The difference between the highest card and the lowest card rank indices is ==4
        :return: True if the hand is a straight, False otherwise
        """
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.num_matches == 0 and distance == 4

matches=0
count=0
while matches<1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count+=1
    if hand.is_straight:
        #print(hand)
        matches+=1
        #break

print(f"The probability of straight is {100*matches/count}%")



