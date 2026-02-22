
def sum_list(list1):
    total_sum = 0
    for index in range(len(list1)):
        total_sum += list1[index]
    return total_sum

list1 = [1, 2, 3, 4, 5, 6]
print(sum_list(list1))