#my_num = 10
#my_second_num = 5

#while my_num > 0:
#    print("first num = %s" % my_num)
#    my_num -= 2
#    while my_second_num < 20:
#        print("Second num %s" % my_second_num)
#        my_second_num += 5

#print("This is going to print when?")

#han_description = ['stuck-up', 'half-witted', 'scruffy-looking', 'nerf herder']
#print(han_description)
#han_description[2] = "Who's Scruffy Looking"
#han_description[3] = "Master Pilot"

#print(han_description)


#After the user enters a number it prints all the numbers the user has entered and ask for another number to be entered.
#Let the user know if they enter 0 it will do the addition. Then when they push enter it does the addition and prints the results.
#(Challenge) You cannot use an if statement.
#(Extra Challange)The only variables allow are "number", "numbers", and "result" (IE only 3 variables allowed and they are all named those specific things)
#(Extra Extra) do not have the List print with the 0 at the end of the list.

#numbers = []
#ask_for_number = int(input("Give me a number:\n"))

#for i in range(0, ask_for_number):
#    print(numbers)
#    new_input = int(input())
#    numbers.append(new_input)
#    if ask_for_number == 0:
#        print("We can add a 0, but this will end your list.\n")
#        numbers += 1
#        exit()
#print("The new list is: ", numbers)


""" number = None
numbers = []
while number != 0:
    try:
        number = int(input("Please give a number to add (Pressing 0 will do the addition.)\n"))
    except ValueError:
        print("You must give a valid number!")
        number = None
    
    else:
        while number:
            numbers.append(number)
            break
            print(numbers)
        
    print(numbers)

result = sum(numbers)
print(result) """



#Create a program that prints the ingredients of your 3 favorite foods. 
#The ingredients must be in a list inside of the foods list
#Before each food print "Food # X has the following ingredients". Where X is the index of the food.
#(Challange) You can only use the for in operation.
#(Extra Challenge) Make it a quiz game of guess the food based on its ingredients. Add more food items if needed.

#print(f'Food {x_1} has the follow ingredients: {pizza}.')

""" pizza = ['Pizza', 'pepperoni', 'cheese', 'dough']
tacos = ['Tacos' , 'tortillas', 'ground meat', 'vegetables']
pasta = ['Pasta', 'noodles', 'sauce']

favorite_foods = [pizza, tacos, pasta]
#print(favorite_foods)

for food in favorite_foods:
    print("Food %s has the following ingredients: %s" % favorite_foods[0]), (favorite_foods[1:])) """


food_list = [
    ['pepperoni', 'cheese', 'dough'],
    ['tortillas', 'ground meat', 'vegetables'],
    ['noodles', 'sauce']
]

idx = 0
for food in food_list:
    print("Food #%s has the following ingredients: " % idx)
    for i in food:
        print("    %s" % i)
    idx += 1