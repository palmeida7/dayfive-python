#python dictionaries
#an unordered collection of key value pairs

""" names_and_force = {
    "Luke":"light",
    "Maul":"dark",
    "Han":"grey",
    "Yoda":"light"
}
print(names_and_force) """

""" ##can also have other types inside the dictionary
ex =  {
   "light":["Luke", "Yoda"] ,
    "number": [1,2],
}
print(ex)
#can print key same as an index
print(ex["number"])
print(ex["light"][0]) """

foods = {
    "fruits":['banana', 'orange'],
    "meats":["chicken", 'pork'],
    "grains":["bread", "oatmeal"]
}
print(foods)
if "grains" in foods:
    print("We will make toast.")
else:
    print("Go to the store.") """

""" #del from dictionaries
#adding
#replacing
print("Do we have strawberries?")
#find w/in dictionaries
if "strawberry" in foods:
    print("Eat breakfast")
else:
    print("Need to buy some.") """

""" for key in foods:
    print(foods[key])
    print(key)
 """


##Adding a new item into a list of a key in a dictionary
foods["fruits"].append("strawberry")
#print(foods)
print(foods["fruits"])
print(foods)