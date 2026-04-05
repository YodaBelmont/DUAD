from datetime import datetime
from numbers import Number
from functools import wraps


def validate_numbers(func):
    @wraps(func)
    def wrapper(num1, num2):
        if isinstance(num1, Number) and isinstance(num2, Number):
            return func(num1, num2)
        print("BOTH ARGUMENTS MUST BE NUMBERS")
        return

    return wrapper


def log_call(func):
    @wraps(func)
    def wrapper(num1, num2):
        today = datetime.now()
        print(f"Now executing {func.__name__}...")
        print(f"Arguments: {num1},{num2}")
        print(f"This is being executed on {today.date()}")
        print(f"At {today.time()}")
        func(num1, num2)

    return wrapper


@validate_numbers
@log_call
def multiply(num1, num2):
    return print(f"Result: {num1 * num2}")


multiply("a", 4)
