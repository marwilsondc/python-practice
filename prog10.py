#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

number_list = range(0, 101)

for i in number_list:
    if i % 10 != 0:
        print(i)
