
from random import choice

def determine_winner(p1, p2)
    '''
    params: choice p1 and p2 are both strings and 
    can be "rock" "paper" or "scissors"

    '''
        winners = {
        "rock":{
            "rock": None, # represents a tie
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None, # represents a tie
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None, # represents a tie
        },
    }
    winning_choice = winners[choice1][choice2]
    return winning_choice

if __name__ == '__main__':
    #
    # USER SELECTION
    #
    VALID_OPTIONS = ["rock", "paper", "scissors"]

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #
    if winner == user_choice:
        print("You Won")
    elif winner == computer_choice:
        print("Computer Won")
    elif winner == None
        print ("Tie")
