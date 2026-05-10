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


def validate_list(list_to_evaluate):
    for item in list_to_evaluate:
        if not isinstance(item, (int, float)):
            raise ValueError("LIST MUST ONLY CONTAIN NUMBERS")

    bubble_sort(list_to_evaluate)
    print("PROGRAM FINISHED")


list1 = [99, "a", 0, 55, 19, 70, 33, 27, 100]

validate_list(list1)
