#Ejercicio 1
def function_1():
    print("Hello")
    function_2()

def function_2():
    print("World")

function_1()

#Ejercicio 2

def function_1():
    age = 0
    print(age)

def function_2():
    global name
    name = "Rodolfo"
    return name

# la variable no esta al alcance global porque la inicializamos dentro de una funcion y solo existe durante el tiempo de ejecucion de esta funcion
age += 3

name = "Esteban"
print(name)
print(function_2())

#Ejercicio 3

def sum_list(list1):
    total_sum = 0
    for index in range(len(list1)):
        total_sum += list1[index]
    return total_sum

list1 = [1, 2, 3, 4, 5, 6]
print(sum_list(list1))

#Ejercicio 4

def slice_string(string):
    reversed_string = ""
    for char in string[len(string)::-1]:
        reversed_string += char
    return reversed_string

print(slice_string("Hello World!"))

#Ejercicio 5

def count_lower_upper(my_string):
    blank_space = 0
    upper_counter = 0
    lower_counter = 0
    for char in my_string:
        if char.isupper():
            upper_counter += 1
        elif char.islower():
            lower_counter += 1
        else:
            blank_space +=1
    return print(f"Upper letters: {upper_counter} Lower letters: {lower_counter} Spaces: {blank_space}")

count_lower_upper("Hello World")

#Ejercicio 6

def alphabetic_string(my_string):
    list1 = my_string.split("-")
    list1.sort()
    ordered_string = "-".join(list1)
    return print(ordered_string)

alphabetic_string("Pizza-Cheese-Map-Ant-Baby")

#Ejercico 7

def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True


def sort_list(my_list):
    prime_list = []
    for num in my_list:
        if is_prime(num):
            prime_list.append(num)
    print(f"Non Prime Numbers: {my_list} ")
    print(f"Prime Numbers list: {prime_list}")

list1 = [1, 2, 5, 7, 9, 3, 10, 17]

sort_list(list1)
