def count_lower_upper(my_string):
    if my_string == "":
        raise TypeError("STRING CANNOT BE IN BLANK")
    blank_space = 0
    upper_counter = 0
    lower_counter = 0
    for char in my_string:
        if char.isupper():
            upper_counter += 1
        elif char.islower():
            lower_counter += 1
        else:
            blank_space += 1
    return print(f"Upper letters: {upper_counter} Lower letters: {lower_counter} Spaces: {blank_space}")


count_lower_upper("Hello World")
