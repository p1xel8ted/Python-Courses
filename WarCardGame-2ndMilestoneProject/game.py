from player import Player
from deck import Deck

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    new_deck.shuffle_deck()
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print(f"Player {player_one.name} is out of cards. Player {player_two.name} wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print(f"Player {player_two.name} is out of cards. Player {player_one.name} wins!")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!")
            if len(player_one.all_cards) < 3:
                print(f"Player {player_one.name} unable to delcare war.")
                print(f"Player {player_two.name} wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print(f"Player {player_two.name} unable to delcare war.")
                print(f"Player {player_one.name} wins!")
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
