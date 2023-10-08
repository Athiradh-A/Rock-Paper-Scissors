import inquirer as inq
from colored import fg,attr,bg
import random 

color = fg(random.randint(1,256))

print(color + "WELCOME TO")
print(color + " - ROCK - PAPER - SCISSORS - ")



user = 0 
comp = 0 

times = "Y"
while times.lower() == "y":
    Question = [
        inq.List("moves",
            message="select your move:",
            choices=["Rock","Paper","Scissors"],
        ),
    ]

    comp_moves = ['Rock','Paper','Scissors']
    comp_index = random.randrange(3)
    comp_choice = []
    comp_choice = comp_moves[comp_index]
    print(comp_choice)


    move = inq.prompt(Question)['moves']
    if move == comp_choice:
        print(color + f"Computer chose {comp_choice}")
        print("DRAW!!")
    elif move.lower() == 'rock' and comp_choice.lower() == 'scissors':
        print(color + f"Computer chose {comp_choice} , User wins!!")
        user += 1
    
    elif move.lower() == 'paper' and comp_choice.lower() == 'rock':
        print(color + f"Computer chose {comp_choice} , User wins!!")
        user += 1 

    elif move.lower() == 'scissors' and comp_choice.lower() == 'paper':
        print(color + f"Computer chose {comp_choice} , User wins!!")
        user += 1 

    elif move.lower() == 'rock' and comp_choice.lower() == 'paper':
        print(fg(124) + f"Computer chose {comp_choice} , User loses!!")
        comp += 1 

    elif move.lower() == 'paper' and comp_choice.lower() == 'scissors':    
        print(fg(124) + f"Computer chose {comp_choice} , User loses!!")
        comp += 1

    elif move.lower() == 'scissors' and comp_choice.lower() == 'rock':
        print(fg(124) + f"Compuer chose {comp_choice} , User loses!!")
        comp += 1 

    else:
        print(color + "no points for both !!")


    continue_loop = [
        inq.List('continue',
        message = 'Want to play again??',
        choices = ['Y','N'],
        ),
    ]

    times = inq.prompt(continue_loop)['continue']


print(color + "TOTAL USER SCORE :", color + str(user))
print(color + "TOTAL COMPUTER SCORE :", color + str(comp))