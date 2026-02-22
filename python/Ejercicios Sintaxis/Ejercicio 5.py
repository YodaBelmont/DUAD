total_grades = int(input("How many grades do you want to evaluate?: "))
failed_grades = 0
approved_grades = 0
grade  = 0
total_average = 0
approved_average = 0
failed_average = 0
total_sum = 0
approved_sum = 0
failed_sum = 0

for i in range(total_grades):
    grade = int(input("Enter your grade: "))
    if grade < 0:
        grade = 0

    total_sum += grade

    if grade >= 70:
        approved_sum += grade
        approved_grades += 1
    else:
        failed_grades += 1
        failed_sum += grade

if approved_grades > 0:
    approved_average = approved_sum / approved_grades
else:
    approved_average = 0

if failed_grades > 0:
    failed_average = failed_sum / failed_grades
else:
    failed_average = 0

if total_grades > 0:
    total_average = total_sum / total_grades
else:
    total_average = 0

print(f"Failed grades: {failed_grades}")
print(f"Approved grades: {approved_grades}")
print(f"Overall average: {total_average}")
print(f"Approved grades average: {approved_average}")
print(f"Failed grades average: {failed_average}")

print(f"Failed grades: {failed_grades}")
print(f"Approved grades: {approved_grades}")
print(f"Overall average: {total_average}")
print(f"Approved grades average: {approved_average}")
print(f"Failed grades average: {failed_average}")