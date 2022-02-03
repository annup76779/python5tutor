"""
Dart game simulation.
Author: Thomas Lacombe
"""
import random
import math

def main():
    username = "aban377" #Add your username here
    number_of_player1_wins = 0
    number_of_player2_wins = 0
    number_of_draws = 0
    print_banner(username)
    print()
    print_menu()
    user_choice = get_user_input()
    while user_choice == 1:
        print()
        print_separator()
        result_player1 = get_num_throws_to_reach_501()
        print_player_throws("Player 1", result_player1)
        result_player2 = get_num_throws_to_reach_501()
        print_player_throws("Player 2", result_player2)
        if result_player1 < result_player2:
            print("Player 1 wins.")
            number_of_player1_wins += 1 
        elif result_player1 > result_player2:
            print("Player 2 wins.")
            number_of_player2_wins += 1
        else:
            print("This is a draw.")
            number_of_draws += 1
        print()
        print_separator()
        print_menu()
        user_choice = get_user_input()
    print()
    print_separator()    
    print_stats(number_of_player1_wins, number_of_player2_wins,number_of_draws)
    print_separator()
    
#Paste your completed functions here

# function to print separator
def print_separator():
    # prints out a line of 37 "-" characters
    print("-"*37)

# function to print the banner message
def print_banner(user_name):

    # create a string adding the message to username
    character = '-'
    message = 'Darts game simulator 1.0 by '+user_name
    line = character*len(message)
    # print the message between two lines made up of '-'s
    print(line)
    print(message)
    print(line)

# printing the menu for the game
def print_menu():
    print("Please select an option:")
    print("Enter 1 to play a darts game.")
    print("Enter 0 to exit.")

# get the user input function 
def get_user_input():
    userIn = int(input("Please enter your choice: "))
    while True:
        if userIn == 0:
            return 0
        elif userIn == 1:
            return 1
        userIn = int(input("Error. Please enter a valid choice: "))


# function to get the number of times a player had to throw the darts to get over 501 
def get_num_throws_to_reach_501():
    return num_throws()

# helper function for get_num_throws_to_reach_501()  
def num_throws(current_score = 0, score = 501):
    sub = score - current_score
    if sub <= 0:
        return 0
    new_score = get_score_throw(get_distance_to_centre(get_dart_throw(-5, 5)))
    return 1 + num_throws(current_score = new_score, score = sub)

# function to determine the score of the user based on the distance_to_centre
def get_score_throw(distance_to_centre):
    if is_bullseye(distance_to_centre):
        return 100
        
    elif is_50(distance_to_centre):
        return 50
        
    elif is_20(distance_to_centre):
        return 20
        
    elif is_10(distance_to_centre):
        return 10
        
    elif is_out(distance_to_centre):
        return 0


# fucntion to get the distance between coordinates and center
def get_distance_to_centre(string_coordinates):
    x, y = [float(i) for i in string_coordinates.split()]
    distance = ((x ** 2) + (y ** 2)) ** 0.5
    return round(distance, 2)

#get the coordinates
def get_coordinate(lower_bound,upper_bound):
    coordinate=round(random.uniform(lower_bound,upper_bound),2)
    return coordinate

#function definiton
def get_dart_throw(lower_bound,upper_bound):
    x=get_coordinate(lower_bound,upper_bound)
    y=get_coordinate(lower_bound,upper_bound)
    return f"{round(x, 2)} {round(y, 2)}"


# throws taken by the user to get to pass over 501 scores is printed by this function
def print_player_throws(name_player, number_of_throws):
    print(f'{name_player} reached 501 with {number_of_throws} throws.')


# printing the states after the game is over
def print_stats(num_player1_wins, num_player2_wins, num_draws):
    # Print Stats
    print(f'Player 1 won {num_player1_wins} time(s).')
    print(f'Player 2 won {num_player2_wins} time(s).')
    print(f'There was/were {num_draws} draw game(s).')


#-------------------------------------------------------------------------------|
# function to get the score for different distances of the dart from the center |
#-------------------------------------------------------------------------------|

def is_bullseye(distance_to_centre):
    return distance_to_centre <= 1

def is_50(distance_to_centre):
    return distance_to_centre>1.0 and distance_to_centre<=2.0


def is_20(distance_to_centre):
    return distance_to_centre > 2 and distance_to_centre <= 3

def is_10(distance_to_centre):
    return distance_to_centre > 3 and distance_to_centre <= 4

def is_out(distance_to_centre):
    return distance_to_centre > 4
main()