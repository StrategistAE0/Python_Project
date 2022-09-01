#Lesson 3 - Guess the Number  
#Understanding the Basic & Control Flow Statements (While & For Loop)

#Import Library (Random)
import random

#Input Name (String)
Name = input("Enter Your Name : ")
Lower_limit = int(input("Enter Lower Limit :"))
Upper_limit = int(input("Enter Upper Limit :"))
#Range of random number to be generated (0-5)
#random.randint(start, stop)
random_number_generator = random.randint(Lower_limit,Upper_limit)
#help(random.randint)

#Number of try allowed
Number_of_try = 3

while Number_of_try > 0:

    #Input only a number(Integer), replace the Lower_limit and Upper_limit with your value
    print('Enter only number range from "Lower_limit" to "Upper_Limit" ')
    guess_a_number = int(input("Guess a Number : "))
    if guess_a_number not in range(Lower_limit, Upper_limit):
        print("Please enter only number in range of " + str(Lower_limit) + " to " + str(Upper_limit))
        guess_a_number = int(input("Guess a Number : "))

    #Control Flow : If & else statements
    if random_number_generator == guess_a_number:
        print("Your guess correctly!!!")
        break
    elif random_number_generator < guess_a_number:
        print("The number generated is smaller than number you guess")
    else:
        print("The number generated is bigger than number you guess")
    
    #Number of try counter
    Number_of_try = Number_of_try - 1
    #Display number of try available
    print("You have " + str(Number_of_try) + " chance left\n")

