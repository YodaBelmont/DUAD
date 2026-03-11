import re


class student:
    def __init__(
        self,
        full_name,
        group,
        spanish_grade,
        english_grade,
        science_grade,
        social_studies_grade,
    ):
        self.full_name = full_name
        self.group = group
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.science_grade = science_grade
        self.social_studies_grade = social_studies_grade


def create_student(students_list):
    name = get_valid_name()
    group = get_valid_group()
    if student_exist(name, group, students_list):
        return
    student1 = student(name, group, get_grades())
    return student1


def get_grades():
    grades = {}
    assignments = [
        "Spanish grade",
        "English grade",
        "Science grade",
        "Social Studies grade",
    ]
    for subject in assignments:
        grades[subject] = get_valid_grade(subject)
    return grades


def student_exist(name, group, students_list):
    total_dupes = 0
    for student in students_list:
        if student.full_name == name and student.group == group:
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
    while True:
        try:
            grade = int(input(f"Enter {subject}: "))
            if 0 <= grade <= 100:
                return grade
            print("PLEASE ENTER A NUMBER BETWEEN 0 AND 100")
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER")


def show_students_data(students_list):
    if students_list:
        print(students_list)
    else:
        print("NO DATA TO SHOW")


def calculate_average(student):
    total_sum = 0
    subjects = [
        "spanish_grade",
        "english_grade",
        "social_studies_grade",
        "science_grade",
    ]
    for subject in subjects:
        total_sum += student.grades[subject]
    total_sum = total_sum / 4
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
        "spanish_grade",
        "english_grade",
        "social_studies_grade",
        "science_grade",
    ]
    for subject in subjects:
        if student.grades[subject] < 60:
            failed_scores.append(student[subject])
            print(f"Name: {student.full_name}")
            print(f"Group: {student.group}")
            print(f"\n{subject}: {student.grade[subject]}")
    return failed_scores


def get_all_failed_scores(students_list):
    if students_list:
        for student in students_list:
            failed_subjects = get_failed_scores(student)
        if not failed_subjects:
            print("THERE IS NO DATA TO SHOW")
    else:
        return print("THERE IS NO DATA TO SHOW")


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
    match = False
    option = 0
    group = get_valid_group()
    name = get_valid_name()
    for student in students_data:
        if student.full_name == name and group == student.group:
            match = True
            break
    if match:
        print(f"STUDENTS FULL NAME:{name}")
        print(f"STUDENTS GROUP:{group}")
        while True:
            option = int(input("DO YOU WISH TO REMOVE THIS STUDENT?\n1-Yes\n2-No\n:"))
            if option == 1:
                students_data.remove(student)
                return True
            elif option == 2:
                print("ACTION CANCELED")
                return False
            print("PLEASE ENTER A VALID OPTION")
            continue
