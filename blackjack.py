
import random
from time import sleep


def draw(deck):
    new_card = deck[0]
    deck = deck[1:]
    return new_card, deck


def draw_evaluate(card, hand):
    if card[0] in ['J', 'Q', 'K', '1']:
        hand.append(10)
    elif card[0] == 'A':
        hand.append(11)
    else:
        hand.append(int(card[0]))


def sum_hand(hand):
    add_hand = 0
    for x in hand:
        add_hand += x
    return add_hand

player_score = 0
computer_score = 0
exit_game = False
while exit_game is not True:

    player_hand = []
    computer_hand = []
    player_sum = 0
    computer_sum = 0

    # I used 7_cards.py to create the deck
    suits = "\u2663 \u2665 \u2666 \u2660".split()
    values = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

    deck = []
    for suit in suits:
        for face in values:
            deck.append(face+suit)

    random.shuffle(deck)
    player_card_1 = deck[0]
    computer_card_1 = deck[1]
    player_card_2 = deck[2]
    computer_card_2 = deck[3]
    deck = deck[4:]
    print("Player hand: %s %s" % (player_card_1, player_card_2))
    print("The computer card 1:", computer_card_1)

    draw_evaluate(player_card_1, player_hand)
    draw_evaluate(player_card_2, player_hand)
    draw_evaluate(computer_card_1, computer_hand)
    draw_evaluate(computer_card_2, computer_hand)
    player_sum = sum_hand(player_hand)
    computer_sum = sum_hand(computer_hand)

    if player_sum != 21 and computer_sum != 21:
        exit = False
        while player_sum < 21 and exit is False:
            player_draw = input('Do you want another card? (y/n)\n')
            if player_draw == 'y':
                new_card, deck = draw(deck)
                draw_evaluate(new_card, player_hand)
                if sum_hand(player_hand) > 21:
                    for index, value in enumerate(player_hand):
                        if value == 11:
                            player_hand[index] = 1
                player_sum = sum_hand(player_hand)
                print(
                    "Drawn Card: %s, player_total: %s"
                    % (new_card, player_sum))
            elif player_draw == 'n':
                exit = True
            else:
                print("ERROR: invalid input")

        if player_sum <= 21:
            print(
                "computer hand: %s %s, computer total: %s"
                % (computer_card_1, computer_card_2, computer_sum))
            while computer_sum < 17:
                new_card, deck = draw(deck)
                draw_evaluate(new_card, computer_hand)
                if sum_hand(computer_hand) > 21:
                    for index, value in enumerate(computer_hand):
                        if value == 11:
                            computer_hand[index] = 1
                computer_sum = sum_hand(computer_hand)
                sleep(4)
                print(
                    "The computer drew: %s, the computer total: %s"
                    % (new_card, computer_sum))
            if computer_sum > 21:
                player_score += 1
                print("Congratulations you win, The computer busted!")
            elif computer_sum < player_sum:
                player_score += 1
                print("Congratulations you win!")
            elif computer_sum > player_sum:
                computer_score += 1
                print("Sorry the computer won!")
            elif computer_sum == player_sum:
                print("You tied!")
        else:
            computer_score += 1
            print("Sorry you busted, the computer wins!")
    elif player_sum == 21 and computer_sum != 21:
        player_score += 1
        print("Congratulations you got Blackjack!")
    elif player_sum != 21 and computer_sum == 21:
        computer_score += 1
        print("Sorry The computer got Blackjack!")
    else:
        print("You tied!")
    sleep(3)
    print(
        "score:\nplayer: %s\ncomputer: %s\n"
        % (player_score, computer_score))
    play_again = input('Do you want to play again? (y/n)\n')
    if play_again == 'n':
        exit_game = True
