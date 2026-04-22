def reverse_bubble_sort(list_to_sort):
    size = len(list_to_sort)
    for outer_index in range(size - 1):
        changes_made = False
        for index in range(size - 1, outer_index, -1):
            current_number = list_to_sort[index]
            prev_number = list_to_sort[index - 1]
            if prev_number < current_number:
                changes_made = True
                list_to_sort[index] = prev_number
                list_to_sort[index - 1] = current_number

            print(
                f"Iteration: {outer_index} Current number: {current_number} Next number: {prev_number}"
            )
        print(list_to_sort)
        if not changes_made:
            return


list1 = [1, 5, 70, 100]


reverse_bubble_sort(list1)
