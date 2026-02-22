
def alphabetic_string(my_string):
    list1 = my_string.split("-")
    list1.sort()
    ordered_string = "-".join(list1)
    return print(ordered_string)

alphabetic_string("Pizza-Cheese-Map-Ant-Baby")