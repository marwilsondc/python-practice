#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

number_list = set()

odd_list = set()

number = 1

while len(number_list) < 10:
    print("Input no.:", number)
    new_input = int(input("Enter a number: "))
    number_list.add(new_input)
    if new_input % 2 != 0:
        odd_list.add(new_input)
    number += 1
    
print(number_list)
print("The odd numbers are:", odd_list)
print("Total of:", len(odd_list), "odd numbers")
