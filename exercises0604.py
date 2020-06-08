#1
""" num_list = [1,2,3,4] """
""" print(sum(num_list)) """

#2 print the largest of the numbers
""" num_list = [1,3,7,4]
num_list.sort()
print("Our largest number is: ", num_list[-1]) """

#3
#num_list = [10,1,3,2]
#num_list.sort()
#print("Our smallest number is ", num_list[0])

#4 print only even numbers
#num_list = [1,2,3,4,5,6]
#for i in num_list:
#    if i % 2 == 0:
#        print(i)

#5 Create a list of numbers, print each number in the list that is greater than zero.
##A lambda function is a small anonymous function. 
##A lambda function can take any number of arguments, but can only have one expression.
#num_list = [-1,-2,-3,4,5,6]
#pos_list = list(filter(lambda x: x>0, num_list))
#print(pos_list)

#6 Create a list of numbers, create a new list which contains every number in the given list which is positive.
#num_list = [-1,-2,-3,4,5,6]
#evn_list = list(filter(lambda x: x % 2 == 0, num_list))
#print(evn_list)

#7 Given a string, print the string reversed.
#s = "This is cool."
#def yoda_talk(s):
#    str = ""
#    for i in s:
#        str = i + str
#    return str

#print(yoda_talk(s))

#OR 

##s = "Hello world"
#print(s)
#print(s[::-1])

#reverse a list
#p = ["Hello", "world"]
#p.reverse()
#print(p)

#8 Given two lists of numbers of the same length, 
#create a new list by multiplying the pairs of numbers in corresponding positions in the two lists
""" x = [2,2,2]
y = [3,4,5]
mult_list = []
for i in range(0, len(x)):
    mult_list.append(x[i] / y[i])
print(str(mult_list)) """

#Calculate the result of adding the two matrices
#num_list = [[1,2],
#[3,4]]
#a = num_list[0]
#b = num_list[1]
#line_one = [a[0] + b[0], a[1] + b[1]]
#line_two = [b[0]] + b
#print(line_one)
##not finished

#import numpy
#list1,list2 = [1,2,3], [4,5,6]
#print(numpy.add(list1,list2))

#9 Calculate the result of adding the two matrices
#ex
""" ar3 = [
        [2,1,3],
        [3,4,5]
        ]
ar4 = [[5,6,6],[7,8,1]]
add_res = []
i=0
# i for row
# c for column
while i < len(ar3):
    s_ar = []
    c = 0
    while c < len(ar3[0]):
        s_ar.append(ar3[i][c]+ar4[i][c])
        c += 1
    i += 1
    add_res.append(s_ar)
print(add_res) """

#10 Use your solution in Matrix Addition, 
# and extend it to work for a pair of matrices of any size, 
# as long as they have the same size.

#11




