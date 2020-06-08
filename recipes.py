#user_input = str(input("What would you like to make?\n"))

recipes = {"A": {"name": "scrambled eggs", "ingredients": [{"name": "eggs", "amount":"2 eggs"}, {"name":"butter",
            "amount":"2 teaspoons"}, {"name":"black pepper","amount":"a dash"}]},
           "B": {"name": "ham sandwich", "ingredients": [{"name": "bread", "amount":"2 slices"}, {"name":"mayo",
            "amount":"1 spread"}, {"name":"black pepper","amount":"a dash"}]},
           "C": {"name": "tacos", "ingredients": [{"name": "tortilla", "amount":"1 tortilla"}, {"name":"ground meat",
            "amount":"1 cup"}, {"name":"vegetables","amount":"1 cup"}]}}

instructions = {"eggs": {"name": "scrambled eggs", "instructions": [{"action1": "crack the eggs", "action2":"2 eggs"}, {"action3":" place butter in pan",
            "action4":"pour eggs in pan"}, {"action5":"continue to mix until hardened to liking"}]},
           "sandwich": {"name": "ham sandwich", "ingredients": [{"act1": "x", "act2":"2 x"}, {"act3":"x",
            }, {"act4":"x"}]},
           "tacos": {"name": "tacos", "instructions": [{"act1": "x"}, {"act2":"x"}, {"act3":"x"}]}}

A = recipes["A"]
B = recipes["B"]
C = recipes["C"]

eggs = instructions["eggs"]
sandwich = instructions["sandwich"]
tacos = instructions["tacos"]

while True:
    user_input = str(input("What would you like to make? A, B, or C?\n"))
    #try:
    if user_input == "A" or user_input == "B" or user_input == "C":
        print(recipes[user_input])
    else:
        print("Choose a valid selection.")
    #except EOFError:
    #    print("Enter a valid input.")
    second_input = str(input("Are you satisfied with your selection?\n"))
    if second_input == ("yes"):
        print("Your meal will be ready soon.")
    recipe_input= str(input("Do you want to see a recipe?.\n"))
    if recipe_input == "yes":
        instruct_input = str(input("Which item?\n"))
        print(instruct_input)
    else:
        print("We will not disturb you.")
        break
    instruct_input = str(input("Which item?\n"))
    if instruct_input == "eggs" or "sandwich" or "tacos":
        print(instructions[instruct_input])
        break
    else: 
        print("We will not disturb you.")
        break
    if second_input == "no":
            ask_input = str(input("Do you want to choose again?\n"))
            if ask_input == "no":
                print("Have a nice day.")
                exit()
            
