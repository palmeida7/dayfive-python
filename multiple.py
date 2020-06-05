user_name = input("What is your ID?\n")
password = input("What is your password?\n")


if len(user_name) < 6 or len(password) < 6:
   print("The ID and password must be greater than 6 characters")
elif len(user_name) > 12 or len(password) > 12:
    print("The ID and password must be less than 12 characters")

confirm_password = input("Confirm Password \n")
if confirm_password == password:
    if confirm_password.isdigit():
        print("Fail!")
    else:
        print("Success!")
elif confirm_password != password:
    print("The passwords do not match")
elif confirm_password == int(password):
    print("Password cannot be all numbers")
else:
    print("Fail!")

