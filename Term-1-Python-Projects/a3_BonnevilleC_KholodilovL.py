# PROGRAM ID: Assignment 3
# Description: Group 1 Pair Partner: Lev Kholodilov. Assignment 3 is
# about creating a seat reservation system.
# Revision History:
# Created by Christine Bonneville on March 5th, 2025
# Completed for submission by Christine Bonneville on March 10th, 2025

# I added "import sys" in order to exit the program with
# sys.exit() and also used type() to set seat availability
# based on the advice of my Group 1 Pair Partner,
# Lev Kholodilov.

# I created the initialization code with the seating plan list,
# user input rows and seats, and nested lists, so the functions have
# data to use. If I put it in a function, the code does not work,
# and I cannot figure out why.

# FIXME This is the code after removing the duplicate lines of "return
#  to menu" from the add, edit and cancel functions. I had forgot that I
#  had it added to the display seating function.

import sys

seating_plan = []

rows_input = int(input("\nHow many rows in the seating plan? "))
seats_input = int(input("How many seats per row the seating plan? "))
print()

for i in range(1, rows_input + 1):
    number_of_rows = []
    for j in range(1, seats_input + 1):
        number_of_rows += [j]
    seating_plan += [number_of_rows]

# Placed functions according how they run


def display_all_seats(seating_plan):
    """
    Print each row in the list
    :return:
    """
    print("Displaying current seating plan.\n")
    row_index = 1
    for row in seating_plan:
            print(f"Row {row_index}: ",end="")
            for seat in row:
                print(seat, end=" ")
            print()
            row_index = row_index + 1
    print("\nReturning to Main Menu.")


def new_reservation(seating_plan):
    """
    Reserving seats
    :return:
    """
    display_all_seats(seating_plan)
    try:
        user_row = int(input(f"\nPlease Note:"
                             f"\nOnly numbered seats are available.\n"
                             f"\nEnter desired row to reserve: "))
        user_seat = int(input("Enter desired seat to reserve: "))
        if type(seating_plan[user_row-1][user_seat-1]) is int:
            user_name = input(f"\nSeat is available for reservation."
                              f"\n"
                              f"\nEnter your name: ")
            seating_plan[user_row - 1][user_seat-1] = user_name.title()
            print(f"\n{user_name.title()}, your seat has been "
                  f"\nreserved for Row {user_row}, Seat {user_seat}.\n")
            if type(seating_plan[user_row - 1][user_seat - 1]) is int:
                print("\nSeat is unavailable for new reservation.")
            display_all_seats(seating_plan)
            return main_menu()
        else:
            print(f"\nSeat unavailable."
                  f"\nPlease choose another."
                  f"\nReturning to Main Menu.")
            return main_menu()

    except ValueError:
        print(f"\n***Error Function 1: Input invalid.***"
              f"\nPlease try again. Returning to Menu.")
        return main_menu()


def edit_reservation(seating_plan):
    """
    Editing seats
    :return:
    """
    display_all_seats(seating_plan)
    try:
        user_row = int(input(f"\nEnter desired row to edit: "))
        user_seat = int(input("Enter desired seat to edit: "))
        if type(seating_plan[user_row - 1][user_seat - 1]) is int:
            print("\nSeat is currently available for new reservation "
                  "only.")
            return main_menu()
        if type(seating_plan[user_row - 1][user_seat - 1]) is str:
            new_name = input(f"\nEnter a new name to edit the"
                             "\nreservation for "
                             f"Row {user_row}, Seat {user_seat}: ")
            seating_plan[user_row - 1][user_seat - 1] = \
                (new_name.title())
            print(f"\n{new_name.title()}, your seat "
                  f"reservation has been"
                  f"\nedited for Row {user_row}, Seat {user_seat}.")
            display_all_seats(seating_plan)
        return main_menu()

    except ValueError:
        print("\n***Error Function 2: Input invalid.***"
              "\nPlease try again. Returning to Menu.")
        return main_menu()


def cancel_reservation(seating_plan):
    """
    Canceling seats
    :return:
    """
    display_all_seats(seating_plan)
    try:
        confirm_cancel = input(f"\nAre you sure you would like to "
                               f"cancel your seat? y/n: ")
        match confirm_cancel:
            case "y":
                user_row = int(input("\nEnter desired row to cancel: "))
                user_seat = int(input("Enter desired seat to cancel: "))
                if (type(seating_plan[user_row - 1][user_seat - 1]) is
                        str):
                    user_name = input(f"Please enter your name to "
                                      f"cancel:")
                    seating_plan[user_row - 1][user_seat - 1] = \
                        (user_seat)
                    print(f"\n{user_name.title()}, your seat "
                          f"reservation has been \ncancelled "
                          f"for Row {user_row}, Seat {user_seat}.\n")
                    display_all_seats(seating_plan)
                    return main_menu()
                if (type(seating_plan[user_row - 1][user_seat - 1])
                        is int):
                    print("\nSeat not reserved.")
                return main_menu()
            case "n":
               print(f"\nYour reservation was not cancelled.")
               display_all_seats(seating_plan)
               return main_menu()

    except ValueError:
        print("\n***Error Function 3: Input invalid.**"
              "\nPlease try again. Returning to Menu.")
        return main_menu()


def quit_menu():
    """
    User Quit Main menu without break
    :return:
    """
    try:
        user_quit = input(f"Are you sure you want to quit? y/n: ")
        active = True
        while active:
            if user_quit == "y":
                active = False
                print(f"\nThank you for using the seat reservation "
                      f"system."
                      f"\nTa ta for now!")
                sys.exit()
            else:
                display_all_seats(seating_plan)
                return main_menu()

    except ValueError:
        print(("\nError Function 3: Input invalid."
               "\nPlease try again. Returning to Menu."))
        return main_menu()


def main_menu():
    """
    Main Menu
    :return:
    """
    try:
        while True:
            print("\nMain Menu")
            print("-------------------------")
            print("1. Reserve Seats")
            print("2. Edit Reservation")
            print("3. Cancel Reservation")
            print("4. Display All Seats")
            print("5. Exit")
            print("-------------------------")
            choice = int(input("Select An Option: "))
            print()
            match choice:
                case 1:
                    new_reservation(seating_plan)
                case 2:
                    edit_reservation(seating_plan)
                case 3:
                    cancel_reservation(seating_plan)
                case 4:
                    display_all_seats(seating_plan)
                case 5:
                    quit_menu()
                case _:
                    raise ValueError

    except ValueError:
        print("\nError Function Menu: Invalid input."
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

# Program starts here

display_all_seats(seating_plan)

main_menu()


