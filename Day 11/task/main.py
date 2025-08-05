import random
import art

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(user_score, comp_score):
    if user_score == comp_score:
        print("Draw")
    elif user_score == 0:
        print("You Win!")
    elif comp_score == 0:
        print("You Lose!")
    elif user_score == 0:
        print("You Win!")
    elif user_score > 21:
        print("You Lose!")
    elif comp_score > 21:
        print("You Win!")
    elif user_score > comp_score:
        print("You Win!")
    else:
        print("You Lose!")

def calc(target_cards):
    target_score = sum(target_cards)
    if target_score == 21 and len(target_cards) == 2:
        target_score = 0
    if target_score > 21 and 11 in target_cards:
        target_cards.remove(11)
        target_cards.append(1)
        target_score -= 10
    return target_score

def play_game():
    # print logo of blackjack game
    print(art.logo)

    user_cards = []
    comp_cards = []
    user_score = comp_score = -1
    game_over = False

    for itr in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:
        user_score = calc(user_cards)
        comp_score = calc(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            another_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calc(comp_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()