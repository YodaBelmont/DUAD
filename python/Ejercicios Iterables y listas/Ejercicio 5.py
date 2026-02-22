
list1 = []
greater = 0
for i in range(10):
    num = int(input("Enter a number: "))
    list1.append(num)
    if num > greater:
        greater = num

print(list1)
print(f"The greater number is: {greater}")