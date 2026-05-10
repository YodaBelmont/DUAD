def bubble_sort_steps(list_to_sort):
    iterations = 0
    changes = 0
    for outer_index in range(0, len(list_to_sort) - 1):
        changes_made = False
        for index in range(0, len(list_to_sort) - 1 - outer_index):
            current_number = list_to_sort[index]
            next_number = list_to_sort[index + 1]
            if current_number > next_number:
                changes += 1
                changes_made = True
                list_to_sort[index] = next_number
                list_to_sort[index + 1] = current_number

            print(
                f"Iteration: {outer_index} Current number: {current_number} Next number: {next_number}"
            )
        iterations += 1
        if not changes_made:
            print(f"List sorted: {list_to_sort}")
            print(f"Total Iterations: {iterations} Total swaps: {changes}")
            return


list1 = [8, 0, 55, 19, 70, 33, 27, 100]


bubble_sort_steps(list1)
