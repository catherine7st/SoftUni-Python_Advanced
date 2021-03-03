n = int(input())

students_grades = {}
grades_lines = input()

for line in grades_lines:
    student, grade = line.split(" ")
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for (student, grades) in students_grades.items():
    grades_string = " ".join(map(str, grades))
    avg_grade = sum(grades)
    print(f"{student} -> {grades_string} (avg: {avg_grade:.2f}")
