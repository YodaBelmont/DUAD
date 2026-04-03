def is_int(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("PARAMETERS MUST BE NUMBERS")
        func(*args)

    return wrapper


@is_int
def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    print(result)
    return result


multiply_numbers(5, "a", 3)
