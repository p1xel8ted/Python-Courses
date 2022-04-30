from random import shuffle
from card import Card
import card


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in card.suits:
            for rank in card.ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def deal_one(self) -> Card:
        return self.all_cards.pop()
