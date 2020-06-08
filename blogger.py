my_blogs = {"post1": {"name": "how to make scrambled eggs", "instructions": [{"action1": "crack the eggs", "action2":"2 eggs"}, {"action3":" place butter in pan",
            "action4":"pour eggs in pan"}, {"action5":"continue to mix until hardened to liking"}]}}

#print(my_blogs)
#print(my_blogs["post1"])

my_blogs["post2"] = {"name": "how to make a ham sandwich", "ingredients": [{"act1": "x", "act2":"2 x"}, {"act3":"x",}, {"act4":"x"}]}
#print(my_blogs)

post1 = my_blogs["post1"]
post2 = my_blogs["post2"]

#for post in my_blogs:
#    select_input = str(input("which blog would you like to read?\n"))
#    if select_input == "post1":
#        print(my_blogs["post1"])
#    delete_input = str(input("did you like this blog post?\n"))
#    if delete_input == "yes":
#        print("please enjoy your read.")
#        break
#    if delete_input == "no":
#        print("do you want to delete?")
#        for post in my_blogs:
#            user_input = str(input("type the post title to delete.\n"))
 #           if user_input == "post1":
 #               del my_blogs["post1"]
 #               exit
 #           if user_input == "post2":
 #               del my_blogs["post2"]
 #               exit
 #   if select_input == "post2":
 #       print(my_blogs["post2"])
  #      delete_input = str(input("did you like this blog post?\n"))
  #      #break
  #  if select_input == "neither":
  #      print("have a nice day.")
  #      exit()

print(my_blogs)

