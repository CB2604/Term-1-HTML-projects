# PROGRAM ID: Assignment 4
# Description: Group 1 Pair Partner: Lev Kholodilov. Assignment 4 is
# about creating a team roster that can be edited.
# Revision History:
# Created by Christine Bonneville on March 30th, 2025
# Completed for submission by Christine Bonneville on April 11th, 2025

# I'm sorry for this assignment. It's not my best work.
# I'm disappointed by my work for this assignment. My partner
# decided to choose my work to be submitted for marking without
# talking to me first. He showed me his code after he has
# submitted. I did my best to make sense of it and produce something
# decent.

# If it wasn't obvious already, I also had trouble understanding
# Class functions in general.

# I can get my code to run the menu, add players, count how many
# players there are and exit the menu. However, I can't figure out how
# to get it to add points properly, or display the player stats.

import sys

"""Global list to store the player created"""
team_roster = []


class Player:
    """an attempt to represent a player's stats; points is made
    private with the double underscore"""
    players_created = 0

    def __init__(self, name, position, total_points):
        """Initialize player attributes"""
        self.name = name
        self.position = position
        self.__total_points = total_points
        self.__total_points = 0
        Player.players_created+=1

    def player_stats(self):
        """Print player stats"""
        print(f"Player stats: {self.name.title()},"
              f" {self.position.title()}, {self.total_points}")

    def update_points(self, total_points):
        """Function to call private total points and add extra
        points"""
        self.__total_points += total_points

    def get_total_points(self):
        """Calling the private total points attribute"""
        return self.__total_points

    @staticmethod
    def team_name():
        """Static Method to print team name"""
        print("Conestoga Condors Team Roster")

# Function 1: Add Players


def add_player():
    """
    Adding Players to the roster
    :return:
    """
    try:
        name =  input("Enter the player's name in letters only: ")
        position = input("Enter the player's position in letters "
                         "only: ")
        total_points = int(input("Enter the player's points in "
                                 "positive whole numbers only: "))
        if name.isalpha() and position.isalpha() and total_points >= 0:
            player = Player(name, position, total_points)
            team_roster.append(player)
            print(f"The Conestoga Condor named {name} was "
                  f"added successfully!")
        else:
            raise ValueError

    except ValueError:
        print(f"\n***Error Function 1: Input invalid.*** "
              f"\nPlease try again. Returning to Menu.")
        return main_menu()

# Function 2: Add Points


def add_points():
    """
    Updating points by adding more point
    :return:
    """
    try:
        call_name = input("Enter a player's name to add extra points"
                          " to their stats: ")
        if call_name in [i.name for i in team_roster]:
            extra_points = int(input("Enter the extra points to "
                                     "add in positive whole "
                                     "numbers only: "))
            if extra_points > 0:
                for i in team_roster:
                    if i.name == user_input:
                        i.update_points(extra_points)
                        print(f"Player's points have  been "
                                f"updated.")
                        return main_menu()
                else:
                    raise ValueError
            else:
                print("Player is not in the roster.")
                return main_menu()

    except ValueError:
        print(f"\n***Error Function 2: Input invalid.***"
              f"\nPlease try again. Returning to Menu.")
        return main_menu()

# Function 3: Display All Players


def display_team_roster():
    """
    Displaying team roster
    :return:
    """
    try:
        print(Player.team_name())
        print(f"The number of players on the "
                  f"team is {Player.players_created}")
        for i in team_roster:
            print(
                f"\nPlayer Information"
                f"\n------------"
                f"\nName:     {i.name} "
                f"\nPosition: {i.position} "
                f"\nPoints:   {i.get_points()}")
            print()

        print("\nReturning to Main Menu.")
        return main_menu()

    except ValueError:
        print(f"\n***Error Function 3: Input invalid.***"
              f"\nPlease try again. Returning to Menu.")
        return main_menu()

# Function 4: Exit

def quit_menu():
    """User Quit Main Menu without break"""
    try:
        user_quit = input(f"Are you sure you want to quit? y/n: ")
        active = True
        while active:
            if user_quit == "y":
                active = False
                print(f"\nThank you for using the team roster system."
                      f"\nSee you at the next game!")
                sys.exit()
            else:
                print(f"\nYou have not exited the roster system for "
                      f"\nthe Conestoga Condors."
                      f"\nReturning to Main Menu.")
                return main_menu()

    except ValueError:
        print(("\nError Function 4: Input invalid."
               "\nPlease try again. Returning to Menu."))
        return main_menu()

# Function 5: Main menu

def main_menu():

    try:
        while True:
            print("\nMain Menu")
            print("------------------------")
            print("1. Add Player")
            print("2. Add Points")
            print("3. Display All Players")
            print("4. Exit")
            print("------------------------")
            choice = int(input("Select an option from the Main Menu: "))
            print()
            if choice == 1:
                    add_player()
            if choice == 2:
                    add_points()
            if choice == 3:
                    display_team_roster()
            if choice == 4:
                    quit_menu()

    except ValueError:
        print("\nError Function Main Menu: Invalid input."
              "\nPlease try again. Returning to Main Menu.")
        return main_menu()

    except Exception:
        print(f"\n***Error Function Main Menu: "
              f"The system has an error.***\n"
              f"\nRebooting Main Menu."
              f"\nPlease try again.\n"
              f"\nIf issue persists,"
              f"\nplease contact the venue "
              f"\ndirectly at 999-999-9999."
              f"\nThank you.\n")
        return main_menu()


# Run Program from Main Menu
main_menu()