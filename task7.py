# Q-2: Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# Deck Class

# It is class of all possible cards in a deck. Total 52 cards.
# Methods - deal() it will take out one card from the deck of cards.
# Deck of cards should get shuffeled while creating the deck object.
# no of cards remaining in deck - <number> should display on printing any deck object.
# Card class

# It is a class of card
# Atrributes - suit and value
# <suit> of <value> should dsiplay on printing any card object.


import random
class Card:

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.value} of {self.suit}"

     
class Deck:
    def __init__(self):
        self.cards = []
        self.populate_deck()
        self.shuffle()

    
    def populate_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit,value))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def __str__(self):
        return f"Number of cards remaining in deck: {len(self.cards)}"

deck = Deck()
print(deck)
print("Dealing a card:", deck.deal())
print(deck)