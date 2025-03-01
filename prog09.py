#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

number_list = range(0,101)

for i in number_list:
    if i % 2 == 0:
        print(i)