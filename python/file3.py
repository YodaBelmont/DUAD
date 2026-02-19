#Ejercicio 1

hotel_information = {
    "name" : "",
    "stars" : "",
    "rooms" : 
    [
        {
        "number" : 1,
        "floor" : 1,
        "price per night" : 500 
    },
    {
        "number" : 2,
        "floor" : 1,
        "price per night" : 1500
    },
    {
        "number" : 3,
        "floor" : 2,
        "price per night" : 1000
    }
    ]
}

#Ejercicio 2

list1 = [
    "first_name",
    "last_name",
    "age",
    "hobby"
]
list2 = [
    "Esteban",
    "Matamoros",
    "22",
    "work"
]
my_dict = {}
for index, item in enumerate(list1):
    my_dict[item] = list2[index]
print(my_dict)

#Ejercicio 3
option = 0
employee = {
    "name" : "Juancho",
    "age" : "23",
    "favorite food" : "pizza",
    "role" : "manager"
}
list_keys = []
while True:
    option = int(input(
"""
---Press 1 if you want to delete a value---
---Press 2 to check dictionary values---
---Press 3 to exit---
"""))
    if option == 1:
        item = input("Enter the key you want to delete: ")
        list_keys.append(item)
        employee.pop(item)
    elif option == 2:
        print("---Dictionary info---")
        print(employee)
    elif option == 3:
        break
    else:
        print("---Please enter a valid option---")
