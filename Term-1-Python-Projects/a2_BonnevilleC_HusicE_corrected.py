""" Program ID: a1_BonnevilleC_HusicE
 Description: You will be creating a program that presents the user with a main menu of three options.
 Each menu option will perform a series of calculations, as noted in the instructions below,
 with the third menu option being an option to exit the program.
 Revision History:
    Created by Christine Bonneville on February, 12 2025"""

"""I learned at PAL that you can put a loop (for or while) inside of a function, so I tried it because
I was struggling to get the program to run properly. I also learned that I should be putting the more 
conditions at the top of the process otherwise the loop won't even get to them if the easier conditions
are met first. I was making the error of setting them up like I set up overloading. If I try to alter my
code now, it will not work, so I hope I did it correctly this time."""

import random

def manipulate_values():
    start_num = int(input("Enter a starting random number: "))
    for i in range (start_num +1, start_num +11):
        if i % 2 == 0:
            print(i * 3, end=" ")
        else:
            print(i * 4, end=" ")
    print(" ")

def play_add_game():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    question_sum = num1 + num2
    user_sum = int(input(f"{num1} + {num2}: "))

    while user_sum != question_sum:
        print("Try again!")
        user_sum = int(input(f"{num1} + {num2}: "))
    if user_sum == question_sum:
        print("You got it!")

while True:
    print("\n")
    print("1. Display 10 manipulated values")
    print("2. Math game")
    print("3. Exit")
    select_option=int(input("Select an option:"))

    if select_option == 1:
        manipulate_values()

    elif select_option == 2:
        play_add_game()

        play_again = input("\nWould you like another question: y/n? ")
        if play_again ==  "y":
            play_add_game()

    else:
        print("Thank you for playing, bye!")
        break



