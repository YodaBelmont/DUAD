import random
#Ejercicio 1

print("hello" + " world")
print(str(10) + " age") #Se debe castear el 10 a str ya que python no permite sumar un str y un int
list1 = ["Daniel"+"Esteban"+"Gabriel"]
list2 = ["Andres"+"Alberto"+"Rodolfo"]
print(list1 + list2)
boolean1 = False
boolean2 = True
print(boolean1 + boolean2)#Aparentemente los booleanos son una especie de int, True = 1 False = 0, por lo que si se pueden sumar

#Ejercicio2

name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if (age <= 3):
    print(f"{name} {last_name} its a baby" )
elif(age > 3 and age <= 10):
    print(f"{name} {last_name} its a child" )
elif(age > 10 and age <= 15):
    print(f"{name} {last_name} its a preteenager" )
elif(age > 15 and age <= 18):
    print(f"{name} {last_name} its a teenager" )
elif(age > 18 and age <= 25):
    print(f"{name} {last_name} its a young adult" )
elif(age > 25 and age <= 65):
    print(f"{name} {last_name} its an adult" )
elif(age > 65 and age <= 100):
    print(f"{name} {last_name} its an older adult" )

#Ejercicio 3

number = random.randint(1, 10)
x = 11
while (x != number):
    x = int(input("Please enter a number from 1 to 10: "))

print("You Guessed")


#Ejercicio 4

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

#Ejercicio 5

total_grades = int(input("How many grades do you want to evaluate?: "))
failed_grades = 0
approved_grades = 0
grade  = 0
total_average = 0
approved_average = 0
failed_average = 0
total_sum = 0
approved_sum = 0
failed_sum = 0

for i in range(total_grades):
    grade = int(input("Enter your grade: "))
    if grade < 0:
        grade = 0

    total_sum += grade

    if grade >= 70:
        approved_sum += grade
        approved_grades += 1
    else:
        failed_grades += 1
        failed_sum += grade

if approved_grades > 0:
    approved_average = approved_sum / approved_grades
else:
    approved_average = 0

if failed_grades > 0:
    failed_average = failed_sum / failed_grades
else:
    failed_average = 0

if total_grades > 0:
    total_average = total_sum / total_grades
else:
    total_average = 0

print(f"Failed grades: {failed_grades}")
print(f"Approved grades: {approved_grades}")
print(f"Overall average: {total_average}")
print(f"Approved grades average: {approved_average}")
print(f"Failed grades average: {failed_average}")


# for i in range(total_grades):
#     grade =  int(input("Enter your grade: "))
#     if(grade >= 70):
#         approved_grades += 1
#         approved_average += grade
#     else:
#         if grade < 0:
#             grade = 0
#         else:
#             failed_average += grade
#         failed_grades += 1
#     total_average += grade

# if failed_average > 0 and failed_grades > 0:
#     failed_average = failed_average // failed_grades
# else:
#     failed_average = 0
# if total_average > 0:
#     total_average = total_average // total_grades
# else:
#     total_average = 0
# if approved_average > 0 and approved_grades > 0:
#     approved_average = approved_average // approved_grades
# else:
#     approved_average = 0

print(f"Failed grades: {failed_grades}")
print(f"Approved grades: {approved_grades}")
print(f"Overall average: {total_average}")
print(f"Approved grades average: {approved_average}")
print(f"Failed grades average: {failed_average}")