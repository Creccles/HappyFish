import playingCard


class HappyFishes:
    playingcard = playingCard.PlayingCard()

    def who_turn(self, hands, number_players, current_player, scored_cards, turn_result):
        if turn_result == "Cards Won":
            return current_player
        elif turn_result == "No Cards Won":
            if current_player == number_players:
                current_player = 0
            else:
                current_player += 1
        return current_player

    def select_player(self, hands, number_players, current_player):
        chosen_player = - 1
        while chosen_player < 0 or chosen_player > int(number_players) and chosen_player != current_player:
            chosen_player = int(input("Which player would you like to ask? ")) - 1

        print("You have chosen Player: ", (chosen_player + 1))
        # vvvvvvvvvvvvvvvvvv
        print(hands[chosen_player], "chosen player hand")
        # ^ONLY FOR TESTING^
        return chosen_player

    def whatToask_player(self, hands, current_player, chosen_player):

        print(hands[current_player], "this is your hand")

        player_card = []

        for index in range(len(hands[current_player])):
            player_card.append(hands[current_player][index][1:])

        whatToAsk = input("What card are you looking for ")

        if whatToAsk in player_card:
            print("You picked a valid card - " + str(whatToAsk) + "'s")
            return whatToAsk
        else:
            print("You DID NOT pick a valid card")
            self.whatToask_player(hands, current_player, chosen_player)

    def card_check(self, hands, current_player, chosen_player, card_picked):

        cards_gained = []
        card = 0
        hand_length = len(hands[chosen_player])

        while card < hand_length:
            if card_picked == hands[chosen_player][card][1:]:
                card_removed = hands[chosen_player].pop(card)
                cards_gained.append(card_removed)
            card += 1
        print(cards_gained)

        if cards_gained:
            print("Congrats you gained the card/s: ", str(cards_gained))
            for card in range(len(cards_gained)):
                hands[current_player].append(cards_gained[card])
            print(hands[current_player])
            return "Cards Won"
        else:
            print("Better luck next time, No " + str(card_picked) + "'s in this hand!")
            return "No Cards Won"

    def main(self):

        current_player = 0
        scored_cards = 0
        turn_result = "Cards Won"

        number_players = int(input("How many players will there be?"))
        deck = self.playingcard.generate_deck()
        deck = self.playingcard.shuffle_cards(deck)
        hands = self.playingcard.deal_cards(deck, 7, number_players)
        print(hands)

        while scored_cards != 52:
            self.who_turn(hands, number_players, current_player, scored_cards, turn_result)
            chosen_player = self.select_player(hands, number_players, current_player)
            card_picked = self.whatToask_player(hands, current_player, chosen_player)
            turn_result = self.card_check(hands, current_player, chosen_player, card_picked)

        #  DISPLAY WINNER


if __name__ == '__main__':
    HappyFishes = HappyFishes()
    HappyFishes.main()

# def hand_score(self, hand):
#      total_score = 0
# temp_dict = {}

#   for index in (len(hand) - 1):
#    hand[index][1]

# for value in playingCard.faces:
#   temp_dict[value] = temp_dict[playingCard.faces[value]]

# def num_value(self, hand):
