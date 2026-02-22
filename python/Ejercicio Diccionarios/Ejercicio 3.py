
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