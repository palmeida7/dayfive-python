#1
""" num_list = [1,2,3,4] """
""" print(sum(num_list)) """

#2 print the largest of the numbers
""" num_list = [1,3,7,4]
num_list.sort()
print("Our largest number is: ", num_list[-1]) """

#3
""" num_list = [10,1,3,2]
num_list.sort()
print("Our smallest number is ", num_list[0]) """

#4 print only even numbers
num_list = [1,2,3,4,5,6,7,8,9,10,11]
num = 0 
while num < len(num_list):
    if num % 2 == 0:
        print(num_list[num], end = " ")

        num += 1