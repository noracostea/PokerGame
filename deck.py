import random
class Card:
    RANKS=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    SUITS=["♣","♦","♥","♠"] #clubs, diamonds, hearts, spades
    def __init__(self,rank,suit):
        """
        Method that creates a card instance by checking if rank and suit are valid, meaning if they are within the lists RANKS and SUITS
        :param rank: a rank
        :param suit: a suit
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank=rank
        self._suit=suit

    @property
    def rank(self):
        """
        Decorator allowing you to access the rank of a card as .rank instead of exposing the internal variable ._rank
        :return: rank
        """
        return self._rank

    @property
    def suit(self):
        """
        Decorator allowing you to access the suit of a card as .suit instead of exposing the internal variable ._suit
        :return: suit
        """
        return self._suit

    def __str__(self):
        """
        Magic method on how to print a card as a string
        :return: string showing the rank and then suit of a card
        """
        return f"{self._rank}{self._suit}"

    # For printing a LIST of cards held within a container (list, dictionary, tuple) we need to use repr
    def __repr__(self):
        """
        Magic method for printing a list of cards held within a container as a cleaner output
        :return:
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Checks if two cards are equal by seeing if they have the same rank
        :param other: card 2
        :return: True if they have the same rank, False if they don't
        """
        return self.rank==other.rank

    #To check if a card is greater/lesser than another we need to compare their POSITIONS in the list RANKS
    def __lt__(self, other):
        """
        Checks if a card is lesser than another by comparing their position in the list RANKS
        :param other: card 2
        :return: True if self less than other, False if other less thank self
        """
        return self.RANKS.index(self.rank)<self.RANKS.index(other.rank)

    def __gt__(self, other):
        """
        Checks if a card is greater than another by comparing their position in the list RANKS
        :param other: card 2
        :return: True if self greater than other, False if other greater thank self
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

class Deck:
    def __init__(self):
        """
        Magic method that initializes a list of cards and loops through every rank and suit, creating a new card object for each combination and appending it to the list
        Assigns the list of all combinations to the instance variable called self._cards
        """
        _cards=[]
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank,suit))
        self._cards=_cards

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
        return str(self._cards)

    def shuffle(self):
        """
        Method to shuffle the list of cards
        :return: list of shuffled cards
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Method to remove and return the top card from the deck
        :return: top card in deck (position 0)
        """
        return self.cards.pop(0)

if __name__=="__main__":
    c1= Card("A","♠") #card created
    print(c1)
    print(c1.suit,c1.rank)
    deck=Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)