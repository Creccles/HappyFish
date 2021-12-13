import playingCard
from src.playingCard import PlayingCard


class HappyFishes:
    playingcard = PlayingCard()

    def who_turn(self, hands, number_players, current_player):
        Scored_cards = 1
        # ^Temporary
        while Scored_cards != 52:

            turn_result = "Cards Won"
            # ^Temporary
            if turn_result == "Cards Won":
                return current_player
            else:
                if current_player == number_players:
                    current_player = 0
                else:
                    current_player += 1
            return current_player
    


    def select_player(self, hands, number_players):
        chosen_player = - 1
        while chosen_player < 0 or chosen_player > int(number_players):
            chosen_player = int(input("Which player would you like to ask?")) - 1

        print("You have chosen Player: ", (chosen_player + 1))
        #vvvvvvvvvvvvvvvvvv
        print(hands[chosen_player], "chosen player hand")
        #^ONLY FOR TESTING^
        return chosen_player


    def ask_player(self, hands, current_player, chosen_player):
        print(hands[current_player], "this is your hand")
        player_card = []

        for index in range(len(hands[current_player]) - 1):
            print(hands[current_player][index][1:])
            player_card = hands[current_player][index][1:]
            #print(player_card[index]) # prints first value then crashes----------------------

        whatToAsk = input('What card are you looking for')

        if whatToAsk in player_card:
            print("You picked a valid card")
        else:
            print("You DID NOT pick a valid card")




    def main(self):

        current_player = 1

        number_players = int(input("How many players will there be?"))
        deck = self.playingcard.generate_deck()
        deck = self.playingcard.shuffle_cards(deck)
        hands = self.playingcard.deal_cards(deck, 7, number_players)
        print(hands)
        self.who_turn(hands, number_players, current_player)
        chosen_player = self.select_player(hands, number_players)
        self.ask_player(hands, current_player, chosen_player)

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