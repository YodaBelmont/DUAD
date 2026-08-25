def slice_string(string):
    if not isinstance(string, str):
        raise TypeError("ARGUMENT MUST BE A STRING")
    if string == "":
        raise TypeError("CANNOT USE A BLANK STRING")
    reversed_string = ""
    for char in string[len(string) :: -1]:
        reversed_string += char
    return reversed_string


print(slice_string("Hello World"))
