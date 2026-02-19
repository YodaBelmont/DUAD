#Ejercicio 1
list_1 = ["Duality", "Somewhere I Belong", "Toxicity"]
list_2 = ["Slipknot", "Linking Park", "System of a Down"]

for index, group in (enumerate(list_2)):
    print(group, list_1[index])

#Ejercicio 2

my_string = input("Enter a String: ")
for char in my_string[len(my_string)::-1]:
    print(char)


#Ejercicio 3
my_list1 = []
list1_size = int(input("Enter list´s size: "))
for i in range(list1_size):
    element = input("Enter something to get into the list: ")
    my_list1.append(element)

print(my_list1)
deleted_element = my_list1.pop(0)
my_list1.insert(0, element)
my_list1.pop(len(my_list1)-1)
my_list1.append(deleted_element)
print(my_list1)

#Ejercicio 4

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = []
even_list= []

for num in my_list1:
    if num % 2 > 0:
        odd_list.append(num)
    else:
        even_list.append(num)

print("Odd numbers list: ")
print(odd_list)
print("Even numbers list: ")
print(even_list)

#Ejercicio 5

list1 = []
greater = 0
for i in range(10):
    num = int(input("Enter a number: "))
    list1.append(num)
    if num > greater:
        greater = num

print(list1)
print(f"The greater number is: {greater}")