"""
A Deck class
"""
from random import shuffle
from card import Card
import card


class Deck:
    """
    A Deck class
    """
    def __init__(self):
        self.all_cards = []
        for suit in card.suits:
            for rank in card.ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        """
        Shuffle the deck.
        """
        shuffle(self.all_cards)

    def deal_one(self) -> Card:
        """
        Take one card from the deck.

        Returns:
            Card: Card object
        """
        return self.all_cards.pop()
