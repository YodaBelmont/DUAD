import csv
import os
import actions


def file_exists():
    if os.path.exists("students_data.csv"):
        return True
    return False


def write_csv(headers, students_data):
    try:
        with open("students_data.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            for student in students_data:
                writer.writerow(student.to_dict())
        return print("DATA EXPORTED SUCCESSFULLY")
    except Exception as error:
        print(error)


def import_csv():
    students_data = []
    assignments = [
        "Spanish grade",
        "English grade",
        "Science grade",
        "Social Studies grade",
    ]
    with open("students_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades = {}
            name = row["Full Name"]
            group = row["Group"]
            for subject in assignments:
                row[subject] = int(row[subject])
                grades[subject] = row[subject]
            student1 = actions.student(name, group, grades)
            students_data.append(student1)
        return students_data
