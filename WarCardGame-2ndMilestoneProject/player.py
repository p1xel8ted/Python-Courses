"""
Player class.
"""
import card as Card


class Player:
    """
    Player class.
    """
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self) -> Card:
        """
        Remove a card from the deck.

        Returns:
            Card: Card object
        """
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """
        Add new cards to the players hand.

        Args:
            new_cards ([Card]): Can be list, or single item.
        """
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.all_cards)} cards."
