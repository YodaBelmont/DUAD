
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
