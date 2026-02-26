import actions
import data

def show_menu():
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
2- Delete Student
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
                actions.delete_student(student_list,input("Enter Students Full Name: "),input("Enter Students Group: "))
            elif option == 3:
                if student_list:
                    print(student_list)
                else:
                    print("NO DATA TO SHOW")
            elif option == 4:
                averages = actions.get_average_student(student_list)
                if averages != 0:
                    actions.show_top_3(averages)
                else:
                    print("NO DATA TO SHOW")
            elif option == 5:
                averages = actions.get_average_student(student_list)
                if averages != 0:
                    print(actions.get_general_average(averages, student_list))
                else:
                    print("NO DATA TO SHOW")
            elif option == 6:
                if student_list:
                    data.write_csv(headers, student_list)
                else:
                    print("THERE IS NO DATA TO EXPORT")
                    print("PLEASE ADD A STUDENT OR IMPORT AN EXISTING FILE")
            elif option == 7:
                if data.file_exists():
                    student_list = data.import_csv()
                else:
                    print("THERE IS NO DATA TO IMPORT")
        except ValueError as error:
            print(f"Error: {error}")