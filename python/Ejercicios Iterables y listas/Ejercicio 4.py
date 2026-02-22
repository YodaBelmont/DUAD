
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