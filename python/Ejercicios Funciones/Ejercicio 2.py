
def function_1():
    age = 0
    print(age)

def function_2():
    global name
    name = "Rodolfo"
    return name

# la variable no esta al alcance global porque la inicializamos dentro de una funcion y solo existe durante el tiempo de ejecucion de esta funcion
age += 3

name = "Esteban"
print(name)
print(function_2())