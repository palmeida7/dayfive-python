#number = input("Pick a number between 10 and 101\n")
#if number.isdigit() == True:
#    if (number < 10 and number > 101):
#        print("A number is required between 10 and 101")
#    else:
#        print("Success!")

########

number = input("Please give a number between 10-101. \n")
try:
    number = int(number)
except ValueError:
    print("This is wrong.")
    exit()
if number == -1:
    print("Clever!")
elif number < 10 or number > 101:
        print("The number must be between 10 and 101")
elif number == 42:
    print("You have read hitchhikers guide to the galaxy!")
else:
    print("You followed instructions. %s is your number." % number)

   
   
   