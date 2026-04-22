def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        changes_made = False
        for index in range(0, len(list_to_sort) - 1 - outer_index):
            current_number = list_to_sort[index]
            next_number = list_to_sort[index + 1]
            if current_number > next_number:
                changes_made = True
                list_to_sort[index] = next_number
                list_to_sort[index + 1] = current_number

            print(
                f"Iteration: {outer_index} Current number: {current_number} Next number: {next_number}"
            )
        print(list_to_sort)
        if not changes_made:
            return


list1 = [77, 55, 46, 90, 12, -7, 0]


bubble_sort(list1)
