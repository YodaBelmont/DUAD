import actions
import data


def show_menu():
    student_list = []
    headers = ("Full Name", "Group", "Grades")
    while True:
        try:
            option = int(
                input(
                    """
STUDENTS MANAGEMENT SYSTEM
-------------------------
WELCOME
-------------------------
Please, select an option:
-------------------------
1- Add Student
2- Delete Student
3- Show students data
4- Show top 3 best students
5- Show average score
6- Show failed scores
7- Export all current data
8- Import data
9- Exit
-------------------------
"""
                )
            )
        except ValueError:
            print("PLEASE ENTER A NUMBER BETWEEN 1 AND 8")
            continue
        if option == 1:
            student = actions.create_student(student_list)
            if student:
                student_list.append(student)
        elif option == 2:
            actions.delete_student(student_list)
        elif option == 3:
            actions.show_students_data(student_list)
        elif option == 4:
            actions.show_top_3(student_list)
        elif option == 5:
            actions.get_general_average(student_list)
        elif option == 6:
            actions.get_all_failed_scores(student_list)
        elif option == 7:
            if student_list:
                data.write_csv(headers, student_list)
            else:
                print("THERE IS NO DATA TO EXPORT")
                print("PLEASE ADD A STUDENT OR IMPORT AN EXISTING FILE")
        elif option == 8:
            if data.file_exists():
                student_list = data.import_csv()
            else:
                print("THERE IS NO DATA TO IMPORT")
        elif option == 9:
            print("Exiting program...")
            break
        else:
            print("PLEASE ENTER A NUMBER BETWEEN 1 AND 8")
