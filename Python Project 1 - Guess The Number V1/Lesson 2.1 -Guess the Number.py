#Lesson 2 - Guess the Number  
#Understanding the Basic & Control Flow Statements (If)

#Import Library (Random)
import random

#Input Name (String)
Name = input("Enter Your Name : ")
#Range of random number to be generated (0-5)
#random.randint(start, stop)
random_number_generator = random.randint(0,10)
#help(random.randint)

#Input only a number(Integer)
guess_a_number = int(input("Guess a Number : "))

#Control Flow : If & else statements
if random_number_generator == guess_a_number:
    print("Wow, you are Cool & Lucky!!!")
else:
    print("Better luck next time!")
    
    
    