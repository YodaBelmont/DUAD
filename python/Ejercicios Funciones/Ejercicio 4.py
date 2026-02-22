
def slice_string(string):
    reversed_string = ""
    for char in string[len(string)::-1]:
        reversed_string += char
    return reversed_string

print(slice_string("Hello World!"))
