import actions
import data

def show_menu():
    if data.file_exists:
        student_list = data.import_csv()
    else:
        student_list = []
    headers = ("Full Name", "Group", "Spanish grade", "English grade", "Social Studies grade", "Science grade")
    option = 0
    while True:
        option = int(input("""
STUDENTS MANAGEMENT SYSTEM
-------------------------
WELCOME
-------------------------
Please, select an option:
-------------------------
1- Add Student
2- Show students data
3- Show top 3 best students
4- Show average scores
5- Export all current data
6- Import data
7- Exit 
-------------------------
"""))
        try:
            if option == 1:
                student = actions.create_student()
                student_list.append(student)
            elif option == 2:
                print(student_list)
            elif option == 3:
                averages = actions.get_average_student(student_list)
                actions.show_top_3(averages)
            elif option == 4:
                print(actions.get_average_student(student_list))
            elif option == 5:
                data.write_csv(headers)
        except ValueError as error:
            print(f"Error: {error}")
    