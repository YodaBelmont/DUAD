def sum_list(list1):
    total_sum = 0
    for index in range(len(list1)):
        total_sum += list1[index]
    return total_sum


list1 = [-1, -5, -9]
print(sum_list(list1))
