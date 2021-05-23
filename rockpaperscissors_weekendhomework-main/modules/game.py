from modules.player import Player

def play(choice_1,choice_2):
    if choice_1 == "rock" and choice_2 == "scissors":
        return "Player 1!"
    elif choice_1 == "rock" and choice_2 == "paper":
        return "Player 2"
    elif choice_1 == "rock" and choice_2 == "rock":
        return "nobody, as its a Draw"
    elif choice_1 == "paper" and choice_2 == "rock":
        return "Player 1"
    elif choice_1 == "paper" and choice_2 == "scissors":
        return "Player 2"
    elif choice_1 == "paper" and choice_2 == "paper":
        return "nobody, as its a Draw"
    elif choice_1 == "scissors" and choice_2 == "rock":
        return "Player 2"
    elif choice_1 == "scissors" and choice_2 == "paper":
        return "Player 1"
    elif choice_1 == "scissors" and choice_2 == "scissors":
        return "nobody, as its a Draw"




    
    
