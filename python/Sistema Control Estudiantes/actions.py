def create_student():
    student = {}
    while True:
        print("""
-------------------------
ENTER STUDENT DATA
-------------------------
""")
        student["Full Name"] = input("Full Name -> ")
        student["Group"] = input("Group -> ")
        while True:
            try:
                student["Spanish grade"] = int(input("Spanish grade -> "))
                student["English grade"] = int(input("English grade -> "))
                student["Social Studies grade"] = int(input("Social Studies grade -> "))
                student["Science grade"] = int(input("Science grade -> "))
                return student
            except ValueError as error:
                print(error)


def get_average_student(students):
    averages = []
    average = 0
    for student in students:
        average += int(student["Spanish grade"])
        average += int(student["English grade"])
        average += int(student["Social Studies grade"])
        average += int(student["Science grade"])
        average = average / 4
        averages.append(average)
        average = 0
    return averages


def show_top_3(averages):
    for index in range(len(averages)):
        greater = max(averages)
        print(f"{greater}")
        averages.remove(greater)
    return 0