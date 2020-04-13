"""
Huang Ching Han
113510994
09/13/19

Assignment 3 : Game of Chance
I used while loop to start the game when the user want to play. If the user inputs 'yes', the game will start, and randomly give three numbers and the matched points.
And then ask the user if they want to play again, if the answer is 'yes', the new three numbers and matched points will be given; if the answer is 'no', the program will
exit.

"""

import random

answer = input("Would you like to play my Game-of-Chance? ")
score = 0

if answer == 'no':
    print("Your score is ", score)
    """ Exit"""

while answer == 'yes':
    number1 = random.randint(1,7)
    number2 = random.randint(1,7)
    number3 = random.randint(1,7)

    print("You rolled a ", number1, "-", number2, "-", number3, ".")

    if (number1 == 7) and (number2 == 7) and (number3 == 7):
        points = 100
    elif (number1 != 7) and (number2 != 7) and (number3 != 7) and (number1 == number2) and (number1 == number3):
        points = 50
    elif (number1 != 7) and (number2 == 7) and (number3 == 7):
        points = 40
    elif (number1 == 7) and (number2 != 7) and (number3 == 7):
        points = 40
    elif (number1 == 7) and (number2 == 7) and (number3 != 7):
        points = 40   
    elif (number1 != 7) and (number2 != 7) and (number1 == number2):
        points = 20
    elif (number1 != 7) and (number3 != 7) and (number1 == number3):
        points = 20
    elif (number2 != 7) and (number3 != 7) and (number2 == number3):
        points = 20 
    elif (number1 != 7) and (number2 != 7) and (number3 == 7) and (number1 != number2):
        points = 10
    elif (number1 != 7) and (number2 == 7) and (number3 != 7) and (number1 != number3):
        points = 10
    elif (number1 == 7) and (number2 != 7) and (number3 != 7) and (number2 != number3):
        points = 10 
    else:
        points = -20
    #print(points)
    score = score + points

    print("That's worth ", points, " points.")
    print("You now have ", score, " points total.")

    answer = input("Would you like to continue playing my Game-of-Chance? ")
    
print("Thanks for playing.")
