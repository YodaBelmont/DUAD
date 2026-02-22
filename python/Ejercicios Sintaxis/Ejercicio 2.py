name = input("Enter your Name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

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