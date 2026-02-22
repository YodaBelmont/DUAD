def sum_numbers(actual_num):
    num2 = int(input("Enter the second number: "))
    total = actual_num + num2
    print(f"Result: {total} \n")
    return total


def subtract(actual_num):
    num2 = int(input("Enter the second number: "))
    total = actual_num - num2
    print(f"Result: {total} \n")
    return total


def multiplication(actual_num):
    num2 = int(input("Enter the second number: "))
    total = actual_num * num2
    print(f"Result: {total} \n")
    return total


def division(actual_num):
    num2 = int(input("Enter the second number: "))
    try:
        total = actual_num / num2
        print(f"Result: {total} \n")
        return total
    except ZeroDivisionError as error:
        print(f"Cannot divide by 0: {error} \n")


def menu():
    while True:
        try:
            actual_num = int(input("Enter a number: "))
            break
        except ValueError as error:
            print(f"An Exception has occurred: {error} \n")
    while True:
        print(
"""Select an Option
1- Addition
2- Subtraction
3- Multiplication
4- Division
5- Delete result
6- Exit""")
        try:
            option = int(input(""))
            if option == 1:
                actual_num = (sum_numbers(actual_num))
            elif option == 2:
                actual_num = (subtract(actual_num))
            elif option == 3:
                actual_num = (multiplication(actual_num))
            elif option == 4:
                actual_num = (division(actual_num))
            elif option == 5:
                try:
                    actual_num = int(input("Enter a number: "))
                except ValueError as error:
                    print(f"An Exception has occurred: {error}\n")
            elif option == 6:
                break
        except Exception as ex:
            print(f"Error: {ex}\n")

menu()