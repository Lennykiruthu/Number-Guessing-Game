import random
import math

#Taking inputs
lower = int(input("\nEnter a lower bound: "))
print("\nLower bound is: " + str(lower))
upper = int(input("\nEnter an upper bound: "))
print("\nUpper bound is:" + str(upper))

#Generating a random number between the upper and lower bound 
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower, 2))," chances to guess the integer!\n")

#Initializing the number of guesses 
count = 0

#For calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower, 2):
    count += 1
    
    #Taking guessing number as input
    guess = int(input ("Guess a number: "))

    #condition testing
    if x==guess:
        print("Congratulation, you guessed it in your", count, "try")

        #Once guessed loop will break
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guessed too high")
        
    #If guessing is more than the required, show this output
    if count >= math.log(upper - lower, 2):
        print("\nThe number is " + str(x))

    #If the guessed number is either lower than the lower bound or higher than the upper bound
    if guess < lower:
        print("You guessed a number below your lower bound")
    elif guess > upper:
        print("You guessed a number above your upper bound")


