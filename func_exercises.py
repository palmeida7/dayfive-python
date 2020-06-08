""" #1. Madlib function
Write a function that accepts two arguments: a name and a subject.

The function should return a String with the name and subject interpolated in.

For example:

madlib("Jenn", "science")
# "Jenn's favorite subject is science."

madlib("Jeff", "history") """
# "Jeff's favorite subject is history."
#Provide default arguments in case one or both are omitted.

""" def favorite(name, subject):
    return (f"{name}'s favorite subject is {subject}.")

print(favorite("Jenn", "science"))
print(favorite("Jeff", "history")) """

########

#2. Celsius to Fahrenheit conversion
#The formula to convert a temperature from Celsius to Fahrenheit is:

#F = (C * 9/5) + 32

#Write a function that takes a temperature in Celsius, converts it Fahrenheit, and returns the value

#import math
""" F= 0
def conversion(C, F):
    return (C * 9/5) + 32

print(conversion(20, F)) """


#3. Fahrenheit to Celsius conversion
""" The formula to convert a temperature from Fahrenheit to Celsius is:

C = (F - 32) * 5/9

Write a function that takes a temperature in Fahrenheit, converts it to Celsius, and returns the value. """

#import math
""" C = 0
def conversion(F, C):
    return (F - 32) * 5/9

print(conversion(70, C)) """

#4. is_even function
#Write a function that accepts a number as an argument and returns a Boolean value. 
#Return True if the number is even; return False if it is not even.



""" x = int(input("Please give a number:\n"))
def even(x):
    if x % 2 == 0:
        print("This is even.")
        return True
        
    else:
        print("This is odd.")
        return False
print(even(x))
 """
#OR

""" def even(num):
    res = False
    if num % 2 ==0:
        res = True
    return res
print(even(2))
print(even(3)) """


#5. is_odd function
#Write an is_odd function that uses your is_even function to determine if a number is odd. 
#(That is, do not do the calculation - call a function that does the calculation.)

#Hint: You'll use the not keyword

""" x = int(input("Please give a number:\n"))
def even(x):
    if not x % 2 == 0:
        print("This is odd.")
        return True
        
    else:
        print("This is even.")
        return False
print(even(x)) """

#########

#6. only_evens function
#Write a function that accepts a List of numbers as an argument.

#Return a new List that includes the only the even numbers.

#only_evens([11, 20, 42, 97, 23, 10])
# Returns [20, 42, 10]
#Hint: use your is_even() function to determine which numbers to include in your new List

""" def is_evens(list):
    even_list = []
    for i in list:
        if i % 2 ==0:
            even_list.append(i)
    return even_list
print(is_evens([11, 20, 42, 97, 23, 10])) """


 #7. only_odds function
#Write a function that accepts a List of numbers as an argument.

#Return a new List that includes the only the odd numbers.
""" def odd(list):
    odd_list = []
    for i in list:
        if i % 2 !=0:
            odd_list.append(i)
    return odd_list
print(odd([11, 20, 42, 97, 23, 10])) """

#1 medium
#1. Find the smallest number
#Write a function smallest that accepts a List of numbers as an argument.

#It should return the smallest number in the List

""" list = [11, 20, 42, 97, 23, 10]
def small(list):
    return min(list)

print(small(list)) """

#2. Find the largest number
#Write a function largest that accepts a List of numbers as an argument.

#It should return the largest number in the List.

""" list = [11, 20, 42, 97, 23, 10]
def large(list):
    return max(list)

print(large(list)) """

######################

##3. Find the shortest String
#Write a function shortest that accepts a List of Strings as an argument.

#It should return the shortest String in the List.

""" strings = ["Hello world", "Is anyone out there", "Guess I am alone"]
calc = min(strings, key = len)

def shortest(strings):
    for i in strings:
        return calc
print(shortest(strings))  """

##2. Find the largest number
#Write a function largest that accepts a List of numbers as an argument.
#It should return the largest number in the List.

""" strings = ["Hello world", "Is anyone out there", "Guess I am alone"]
calc = max(strings, key = len)

def largest(strings):
    for i in strings:
        return calc
print(largest(strings)) """

#######