# world_cup_cosc1336

# This World Cup program was a prompt for my first exam in my Programming Fundamentals I class using Python.

# Program: WorldCup 
# Description: 
#   Simulates playing World Cup tournament games
#
#   main program loops asks if the user wants to play
#   as long as the user wants to play, the program
#       asks for the name of team 1
#       asks for the name of team 2
#       calls function game() with the team names as parameters
#       prints the name of the winner (game() returns this name)
#       asks if the user wants to play again
#
# Author: Allison Crenshaw 
# Date: 07/03/19
# Revised: 
# 	<revision date>
# 	<revision date>

# list libraries used
#   random

# Declare global constants (name in ALL_CAPS)
#   no global constants used in this program

# End template, begin program
import random


def main():
    # Declare and INITIALZE Variables (EVERY variable used in this main program)
    team1_name = ''
    team2_name = ''
    again = ''
    winner = ''

    print("\nWelcome to the Women's World Cup 2019!")

    again = 'y'

    # start while loop
    while again == 'y':
        # starting menu, input for team names
        print('\nWhat countries will be fighting for victory in this round?')
        team1_name = input('Enter name for Team 1: ')
        team2_name = input('Enter name for Team 2: ')

        # call game function & give team name parameters
        winner = game(team1_name, team2_name)
        print('\nAnd the winner is...', winner, '!')
        print('***applause***')

        # input to stop the while loop
        print('\nThanks for playing. Would you like to play again?')
        again = input('Type y for yes, or hit any other key to exit: ')

    # end while loop

    print('\nThanks for playing! See you again in 2023!')


# End main() function


# Function game()
# Description:
#	Plays a 90-minute game
#
#   keeps two total scores, one for each team in the parameter list
#   loops through 90 minutes. in each loop
#       for each team
#           add the return value from Minute() to the team's total score
#       display the current score
#   after 90 loops, compare the totals
#       whichever team total is larger, set the return value to that team name
#       if the totals are equal, set the return value to "it's a tie"
#
# Calls:
#	minute()
# Parameters:
#       team1_name  String
#       team2_name  String
# Returns:
#	winner      String

def game(team1_name, team2_name):
    # Declare and INITIALZE Local Variables (NOT parameters)
    result1 = 0
    result2 = 0
    minutes = 0
    team1_score = 0
    team2_score = 0

    # start for loop
    for x in range(90):
        # call minute function twice, once for each team
        # assign return value from minute() to a variable that can be added to running score
        result1 = minute(team1_name)
        result2 = minute(team2_name)

        # increase minute by 1 to keep track of time elapsed
        minutes = (minutes + 1)

        # calculate new scores for this minute
        team1_score = (team1_score + result1)
        team2_score = (team2_score + result2)

        # print current minute and updated scores
        # should look like: Minute 1      USA: 1, Russia: 2
        print('Minute ', minutes, '\t', team1_name, ':', team1_score, team2_name, ':', team2_score)
    # end for loop

    # start if
    if team1_score > team2_score:
        winner = team1_name
    elif team2_score > team1_score:
        winner = team2_name
    else:
        winner = "It's a tie"
    # end if

    # Return the return variable, if any
    return winner


# End Function game()


# Function minute()
# Description:
#	Determines whether goals are scored in this minute
#
#   There is a 5% chance that there is a try in this minute
#	Generate a random number between 0 and 100
#	If the number is less than 5
#           goals is the return value from score()
#	Otherwise goals is 0
#
#       If goals is greater than 0, display a message that this team scored
#
# Calls:
#	score()
# Parameters:
#       team_name   String
# Returns:
#	goals       Integer

def minute(team_name):
    # Declare and INITIALZE Local Variables (NOT parameters)
    attempt = 0
    goals = 0

    # generate random number 0-100 to determine if team attempts to score
    attempt = random.randint(0, 100)

    # start if
    if attempt < 5:
        goals = score()

        # start if
        if goals == 1:
            print(team_name, 'scores! :D ')
        else:
            print(team_name, 'shoots and misses :( ')
        # end if

    else:
        goals = 0
    # end if

    # Return the return variable, if any
    return goals


# End Function minute()


# Function score()
# Description:
#       Determines if a goal is scored
#
#   There is a 10% chance that a goal is scored by this try
#	Generate a random number between 0 and 100
#	If the number is less than 10
#           goal is scored, return value is 1
#	Otherwise return value is 0
#
# Calls:
#	none
# Parameters:
#       none
# Returns:
#	goal    Integer

def score():
    # Declare and INITIALZE Local Variables (NOT parameters)
    kick = 0
    goal = 0

    # generate random number 0-100 to determine if team's try resulted in a goal
    kick = random.randint(0, 100)

    # start if
    if kick < 10:
        goal = 1
    else:
        goal = 0
    # end if

    # Return the return variable, if any
    return goal

# End Function score()


# Determine if program is run as the main or a module
if __name__ == '__main__':
    # This program is being run as the main program
    main()

else:
    pass
    # Do nothing. This module has been imported by another
    # module that wants to make use of the functions,
    # classes, and/or other items it has defined.

