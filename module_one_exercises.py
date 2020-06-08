#name = input("What is your name?\n")
#print("Hello, %s!" % name)

#name = input("WHAT IS YOUR NAME?\n")
#name_length = len(name)
#a_string = ("hello, %s!" % name)
#print(a_string.upper())
#statement = ("YOUR NAME HAS {} LETTERS IN IT! AWESOME!").format(name_length)
#print(statement)

#name = "Peter"
#subject = "history"
#sentence = "{}'s favorite subject in school is {}.".format(name, subject)
#print(sentence)

#### Review this 
#def day_of_the_week(day):
#    if day == int(input(0)):
#        return "Sunday"
#    if day == int(input(1)):
#        print("Monday")
#    if day == int(input(2)):
#        print("Tuesday")
#    if day == int(input(3)):
#        print("Wednesday")
#    if day == int(input(4)):
#        print("Thursday")
#    if day == int(input(5)):
#        print("Friday")
#    if day == 6:
#        print("Saturday")

#day = int(input('Day (0-6)? '))
#if input :6:
#    print("Go to work.")
#else:
#    print("Sleep in.")

#celsius = int("What is the temperature in C?\n")
#convert_to_F = (celsius * 9/5) + 32
#if input == celsius:
#    return convert_to_F


#number = 0
#while (number >= 0) and (number <= 10):
#    print(number)
#    number += 1

#####
#Tip Calculator
#1. Tip Calculator
#Your task is to write a program that calculates how much of a tip to leave at a restaurant.

#Prompt the user for two things:

#The total bill amount
#The level of service, which can be one of the following: good, fair, or bad
#Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

#good -> 20%
#fair -> 15%
#bad -> 10%

#bill_amount = 0
#while bill_amount == 0:
#    try:
#        bill_amount = float(input("How much was your bill?\n"))
#    except ValueError:
#        print("Please input a valid amount with decimals.")
    

#service_level = input("How was the service? Good, fair, or bad?\n")

#tip = 0 
#if service_level == "good":
#    tip = bill_amount * .2
#elif service_level == "fair":
#    tip = bill_amount * .15
#elif service_level == "bad":
#    tip = bill_amount * .1
##else: 
#    tip = float(input("Please enter a specific amount."))



#print("Tip Amount: %s" % tip)
#print("Total Amount: %s" % (bill_amount+tip))

#try:
#    people = int(input("How many people want to split the bill?\n"))
#    if people == 0:
#        people = 1
#except ValueError:
#    people = 1
#    print("Invalid number. Assumes 1.")


#total = (bill_amount+tip)
#split_amount = (total/people)

#print("The amount to split is $%s between everyone." % split_amount)
#print(f"Tip Amount:{tip}")
#print(f"Total Amount: {bill_amount+tip}")

#You will implement a guess the number game where the player has to try
#guessing a secret number until they get it right. For now you will "Hard code"
#the secret number to 5 (just set it to five like secret_number =5).
#You will prompt the player to enter a number again and again, each time
#comparing their input to the secret number. to that, you will need to write
#a while loop. if they guess correctly, you will print "you win!",
#otherwise you will prompt for a number again.

#secret_number = 5
#guess_number = int(input("I am thinking of a number between 1 and 10.\n"))
#while secret_number != guess_number:
    #guess_number = int(input("I am thinking of a number between 1 and 10.\n"))
    #print(guess_number)
    #print(secret_number)
#    if guess_number == secret_number:
#        print("Yes, You win!")
#        exit()
#    if guess_number != secret_number:
#        guess_number = int(input("I am thinking of a number between 1 and 10.\n"))
#        print(guess_number)
#        print("Nope, try again.")
#        continue
    #try:
    #except ValueError:    
        #print("Please only enter a number between 1 and 10.")
#print("Yes! You win!")


#David's Code
import random
user_name = input("What is your username?\n")
u_score = 0
c_score = 0
while True:
    guess_limit = 5
    guesses = 0
    secret_number = random.randint(0, 10)
    while guesses < guess_limit:
        while True:
            try:
                guess = int(input('What is your guess? [Pick an int between 0 and 10]\n'))
                guesses += 1
                break
            except ValueError:
                print('Please print a valid number')
                continue
        if guess == secret_number:
            print("Congrats, you win this round")
            u_score +=1
            break
        else:
            print(f"Guess again, you have {(5-guesses)} guesses left]")
            continue
    if guesses == guess_limit:
        print("Better luck next time!")
        c_score +=1
    again = input(f"Would you like to play again? The current score is {c_score} computer, {u_score} {user_name}\n")
    if again == "yes" or again == "Yes":
        print("Starting another round")
        continue
    else:
        print("That was fun! See ya next time!")
        exit()