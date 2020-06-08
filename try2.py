try:
    first_number = int(input("Number 1\n"))
except ValueError:
    print("First number is not a number.")
    exit()
try:
    second_number = int(input("Number 2\n"))
except ValueError:
    print("First number is not a number.")
    exit()
try:
    print("The result is %s" % (first_number/second_number))
except ValueError:
    print("You input a text.")
except ZeroDivisionError:
    print("You divided by zero.")
    exit() 
print(first_number/second_number)
print("The result is %s" % (first_number/second_number))
