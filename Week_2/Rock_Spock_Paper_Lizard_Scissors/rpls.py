#Ryan Schachte

import random #Random input generated for the computer to choose a random choice to play against the component


def number_to_name(number): #Function to convert the name into a specified number
    if number == 0: 
        return 'Rock'       #If number is 0, return Rock
    elif number == 1:
        return 'Spock'      #If number is 1, return Spock
    elif number == 2:
        return 'Paper'      #If number is 2, return Paper
    elif number == 3:
        return 'Lizard'     #If number is 3, return Lizard
    elif number == 4:
        return 'Scissors'   #If number is 4, return Scissors
    else:
        return 'This input is not programmed!' #Error conditional for invalid input

def name_to_number(name): #Function to convert the number into a specified name
    if name== 'Rock':
        return 0;
    elif name == 'Spock':
        return 1;
    elif name == 'Paper':
        return 2;
    elif name == 'Lizard':
        return 3;
    elif name == 'Scissors':
        return 4;
    else: 
        return 'Name non-existent in the program!';

def rpsls(player_choice):

    #Take the number of the player and convert it to a corresponding name
    user_option = name_to_number(player_choice) #Convert user option string to an integer
    comp_option = random.randrange(0,5) #Generate random computer number from 0 through 4

    calc_diff = (user_option - comp_option) % 5 #Calculate difference between the two using modulo

    if calc_diff == 0: #Difference is 0, then tie
        outcome = "Player and computer tie!"
    elif calc_diff == 1 or calc_diff == 2: #If difference is 1 or 2, then user wins
        outcome = "Player wins!"
    else:
        outcome = "Computer wins!"

    ai_name = number_to_name(comp_option) #convert the ai name
    
    # print results

    print "Player chooses", player_choice
    print "Computer chooses", ai_name
    print outcome

    if player_choice != "scissors":
        print

#The following are test cases
rpsls("Rock")
rpsls("Spock")
rpsls("Paper")
rpsls("Lizard")
rpsls("Scissors")

