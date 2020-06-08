#Given the following dictionary, representing a mapping from names to phone numbers:

""" phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
} """

#Write code to do the following:

""" Print Elizabeth's phone number.
Add an entry to the dictionary: Kareem's number is 938-489-1234.
Delete Alice's phone entry.
Change Bob's phone number to '968-345-2345'.
Print all the phone entries.  """

""" print(phonebook_dict["Elizabeth"])

del (phonebook_dict["Alice"])

ph1 = {'Bob': '968-345-2345'}
phonebook_dict.update(ph1)
print(phonebook_dict) """

#Given the following dictionary:

""" ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
} """
""" Write a python expression that gets the email address of Ramit.
Write a python expression that gets the first of Ramit's interests.
Write a python expression that gets the email address of Jasmine.
Write a python expression that gets the second of Jan's two interests. """


#print(ramit['email'])
#print(ramit['interests'][0])
#print(ramit['friends'][0]['email'])
#print(ramit['friends'][1]['interests'][1])

#3. Friend counter
#Using the dictionary from the Nested dictionaries exercise above, 
# write a function countFriends() that accepts a dictionary as an argument
# and returns a new dictionary that includes a new key friends_count:

#def countFriends(friends):
""" friends_count = len(ramit['friends'])
print(friends_count)
print('friends count: %d' % friends_count) """

#Write a letter_histogram program that asks the user for input,
# and prints a dictionary containing the tally of 
# how many times each letter in the alphabet was used in the word

input_string = input("Enter a word: \n")
ltr_count = {} 
  
for letter in input_string: 
    if letter in ltr_count: 
        ltr_count[letter] += 1
    else: 
        ltr_count[letter] = 1
    #except NameError:
 

print ("The count per letter in '{}' is :\n {}".format(input_string, str(ltr_count)))



