number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))
greater = 0
if(number1 > number2 and number1 > number3):
    greater = number1
elif(number2 > number1 and number2 > number3):
    greater = number2
elif(number3 > number1 and number3 > number2):
    greater = number3

print(greater)