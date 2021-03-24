
from random import choice

def determine_winner(p1, p2)
    '''
    params: choice p1 and p2 are both strings and 
    can be "rock" "paper" or "scissors"

    '''
    #write the code for this function
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

    if u == "rock":
        if c == "rock"
            print("It's a tie!")
        elif c == "paper"
            print("The computer wins")
        elif c == "scissors"
            print("The user wins")

    if u == "paper":
        if c == "rock"
            print("The user wins")
        elif c == "paper":
            print("It's a tie!")
        elif c == "scissors"
            print("The computer wins")


    if u == "scissors":
        if c == "rock"
            print("The computer wins")
        elif c == "paper":
            print("The user wins")
        elif c == "scissors"
            print("It's a tie!")
'''
    if winner == user_choice:
        print("You Won")
    elif winner == computer_choice:
        print("Computer Won")
    elif winner == None
        print ("Tie")
'''