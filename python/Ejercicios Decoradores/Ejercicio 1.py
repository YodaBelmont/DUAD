def print_param_return(func):
    def wrapper(num1, num2):
        print(num1, num2)
        result = func(num1, num2)
        print(result)

    return wrapper


@print_param_return
def addition(num1, num2):
    return num1 + num2


addition(12, 55)
