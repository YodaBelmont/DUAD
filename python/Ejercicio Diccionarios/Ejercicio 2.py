
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