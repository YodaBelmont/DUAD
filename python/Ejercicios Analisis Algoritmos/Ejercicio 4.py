# Es o(1) ya que el bucle for se ejecuta 10 si tiene 10 elementos,
# si tiene menos elementos se ejecuta esa misma cantidad; ej si tiene 7 se ejecuta 7 veces ya que min() compara el 10 y el len y se queda con el menor
# Pero si tiene mas de 10 se ejecuta solo 10 veces


def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)
    for index in range(min(list_len, 10)):
        print(list_to_print[index])
