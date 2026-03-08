import csv
import os


def file_exists():
    if os.path.exists("students_data.csv"):
        return True
    return False


def write_csv(headers, students_data):
    try:
        with open("students_data.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(students_data)
        return print("DATA EXPORTED SUCCESSFULLY")
    except Exception as error:
        print(error)


def import_csv():
    students_data = []
    grades = ["Spanish grade", "English grade", "Science grade", "Social Studies grade"]
    with open("students_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for subject in grades:
                row[subject] = int(row[subject])
            students_data.append(row)
        return students_data
