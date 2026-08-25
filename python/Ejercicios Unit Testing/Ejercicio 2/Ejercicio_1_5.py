def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


def sort_list(my_list):
    prime_list = []
    for num in my_list:
        if is_prime(num):
            prime_list.append(num)
    print(f"Non Prime Numbers: {my_list} ")
    print(f"Prime Numbers list: {prime_list}")
    return prime_list


list1 = [1, 2, 5, 7, 9, 3, 10, 17]

sort_list(list1)
