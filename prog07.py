#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

number_list = {0}

number = 1

while len(number_list) <= 10:
    print("Input no.:", number)
    number_list.add(int(input("Enter a number: ")))
    number += 1

print(number_list)
print(sum(number_list))