import random
import game_data
import art




def select_random():
    return random.choice(game_data.data)

def check_selection(usr_selection, comp_a, comp_b):
    if comp_a["follower_count"] > comp_b["follower_count"]:
        return  usr_selection == "a"
    return  usr_selection == "b"

def play_game():
    is_game_over = False
    score = 0
    selection_b = select_random()
    print(art.logo)
    while not is_game_over:
        selection_a = selection_b
        selection_b = select_random()
        
        print(f"Compare A: {selection_a["name"]}, {selection_a["description"]}, from {selection_a["country"]}")
        print("\n\n")
        print(f"{art.vs}")
        print(f"Compare B: {selection_b["name"]}, {selection_b["description"]}, from {selection_b["country"]}")


        true_selection = True
        while true_selection:
            user_selection = input("Who has more followers? Type 'A' or 'B'").lower()
            if user_selection != "a" and user_selection != "b":
                print("Please type a valid choice")
            else:
                true_selection = False

        guessed = check_selection(user_selection, selection_a, selection_b)
        print(art.logo)
        if not guessed:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")
        else:
            score+=1
            print(f"You're right. Current score: {score}")


play_game()
