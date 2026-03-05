import re


def create_student(students_list):
    student = {}
    while True:
        print(
            """
-------------------------
ENTER STUDENT DATA
-------------------------
"""
        )
        student["Full Name"] = get_valid_name()
        student["Group"] = get_valid_group()
        if student_exist(student["Full Name"], student["Group"], students_list):
            return 0
        while True:
            try:
                student["Spanish grade"] = get_valid_grade("Spanish grade")
                student["English grade"] = get_valid_grade("English grade")
                student["Social Studies grade"] = get_valid_grade(
                    "Social Studies grade"
                )
                student["Science grade"] = get_valid_grade("Science grade")
                return student
            except ValueError as error:
                print(error)


def student_exist(name, group, students_list):
    total_dupes = 0
    for student in students_list:
        if student["Full Name"] == name and student["Group"] == group:
            total_dupes += 1
    if total_dupes > 0:
        print("THERE CANNOT BE DUPLICATES")
        print("THIS INFO WILL NOT BE INCLUDED")
        return True
    return False


def get_valid_group():
    group = input("Group: ")
    while True:
        if re.fullmatch(r"\d{2}[A-Z]", group):
            return group
        else:
            print("PLEASE FOLLOW THE ALLOWED FORMAT")
            print("EXAMPLE: 11B, 12A, etc...")
            group = input("Group: ")


def get_valid_name():
    name = input("Full Name: ")
    while True:
        name = name.strip()
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("NAME CANNOT CONTAIN NUMBERS OR BE IN BLANK")
            name = input("Full Name: ")


def get_valid_grade(subject):
    grade = int(input(f"Enter {subject} grade: "))
    while grade < 0 or grade > 100:
        print("PLEASE ENTER A VALID NUMBER")
        print("BETWEEN 0 AND 100")
        grade = int(input(f"Enter {subject} grade: "))
    return grade


def show_students_data(students_list):
    if students_list:
        print(students_list)
    else:
        print("NO DATA TO SHOW")


def calculate_average(student):
    total_sum = 0
    total_sum += int(student["Spanish grade"])
    total_sum += int(student["English grade"])
    total_sum += int(student["Social Studies grade"])
    total_sum += int(student["Science grade"])
    total_sum = total_sum // 4
    return total_sum


def get_average_student(students):
    averages = []
    if students:
        for student in students:
            average = calculate_average(student)
            averages.append(average)
    else:
        return 0
    return averages


def get_failed_scores(student):
    failed_scores = []
    subjects = [
        "Spanish grade",
        "English grade",
        "Social Studies grade",
        "Science grade",
    ]
    for subject in subjects:
        if student[subject] < 60:
            failed_scores.append(student[subject])
            print(f"Name: {student['Full Name']}")
            print(f"Group: {student['Group']}")
            print(f"\n{subject}: {student[subject]}")
    return failed_scores


def get_all_failed_scores(students_list):
    if students_list:
        for student in students_list:
            get_failed_scores(student)
    else:
        return print("THERE IS NO DATA")


def show_top_3(students):
    averages = get_average_student(students)
    if averages != 0:
        try:
            for index in range(1, 4):
                greater = max(averages)
                print(f"{index}-{greater}")
                averages.remove(greater)
        except Exception as error:
            print("NO MORE DATA TO SHOW")
    else:
        print("NO DATA TO SHOW")
    return 0


def get_general_average(students_list):
    averages = get_average_student(students_list)
    if averages != 0:
        total_sum = 0
        for average in averages:
            total_sum += average
        print("GENERAL AVERAGE:")
        print(total_sum // len(students_list))
        return 0
    else:
        print("NO DATA TO SHOW")


def delete_student(students_data):
    if not students_data:
        print("NO DATA TO DELETE")
        return False
    matches = 0
    option = 0
    group = get_valid_group()
    name = get_valid_name()
    for student in students_data:
        if student["Full Name"] == name and group == student["Group"]:
            print(f"STUDENTS FULL NAME:{name}")
            print(f"STUDENTS GROUP:{group}")
            while True:
                option = int(
                    input("DO YOU WISH TO REMOVE THIS STUDENT?\n1-Yes\n2-No\n:")
                )
                if option == 1:
                    students_data.remove(student)
                    return True
                elif option == 2:
                    print("ACTION CANCELED")
                    return False
                print("PLEASE ENTER A VALID OPTION")
                continue
        else:
            print("THERE ARE NO MATCHES")
            return False
