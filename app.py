from student import Student
from teacher import Teacher
from course import Course
from grade import Grade
from tabulate import tabulate

def main():
    while True:
        print(" School Management System ".center(75, "="))
        print("1. Student Management")
        print("2. Teacher Management")
        print("3. Course Management")
        print("4. Grade Management")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print(" Student Management ".center(50, "="))
                print("1. Add Student")
                print("2. Update Student")
                print("3. Delete Student")
                print("4. Get Student")
                print("5. Get all Students")
                print("6. Exit")
                student_choice = input("Enter your choice: ")

                if student_choice == "1":
                    try:
                        student_id = int(input("Enter student ID: "))
                        name = input("Enter name: ")
                        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                        grade_level = int(input("Enter grade level: "))
                        Student.add_student(student_id, name, date_of_birth, grade_level)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif student_choice == "2":
                    try:
                        student_id = int(input("Enter student ID to update: "))
                        name = input("Enter name (leave blank to skip): ")
                        date_of_birth_str = input("Enter date of birth (YYYY-MM-DD) (leave blank to skip): ")
                        date_of_birth = date_of_birth_str if date_of_birth_str else None
                        grade_level_str = input("Enter grade level (leave blank to skip): ")
                        grade_level = int(grade_level_str) if grade_level_str else None
                        Student.update_student(student_id, name, date_of_birth, grade_level)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif student_choice == "3":
                    try:
                        student_id = int(input("Enter student ID to delete: "))
                        Student.delete_student(student_id)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif student_choice == "4":
                    try:
                        student_id = int(input("Enter student ID to get details: "))
                        student = Student.get_student(student_id)
                        if student:
                            print(f"Student ID: {student[0]}")
                            print(f"Name: {student[1]}")
                            print(f"Date of Birth: {student[2]}")
                            print(f"Grade Level: {student[3]}")
                        else:
                            print("Student not found.")
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif student_choice == "5":
                    students = Student.get_all_students()
                    if students:
                        headers = ["Student ID", "Name", "Date of Birth", "Grade Level"]
                        data = [[s[0], s[1], s[2], s[3]] for s in students]
                        print(tabulate(data, headers=headers, tablefmt="grid"))
                    else:
                        print("No students found.")
                elif student_choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            while True:
                print(" Teacher Management ".center(50, "="))
                print("1. Add Teacher")
                print("2. Update Teacher")
                print("3. Delete Teacher")
                print("4. Get Teacher")
                print("5. Get all Teachers")
                print("6. Exit")
                teacher_choice = input("Enter your choice: ")

                if teacher_choice == "1":
                    try:
                        teacher_id = int(input("Enter teacher ID: "))
                        name = input("Enter name: ")
                        contact_number = input("Enter contact number: ")
                        subject_taught = input("Enter subject taught: ")
                        Teacher.add_teacher(teacher_id, name, contact_number, subject_taught)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif teacher_choice == "2":
                    try:
                        teacher_id = int(input("Enter teacher ID to update: "))
                        name = input("Enter name (leave blank to skip): ")
                        contact_number = input("Enter contact number (leave blank to skip): ")
                        subject_taught = input("Enter subject taught (leave blank to skip): ")
                        Teacher.update_teacher(teacher_id, name, contact_number, subject_taught)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif teacher_choice == "3":
                    try:
                        teacher_id = int(input("Enter teacher ID to delete: "))
                        Teacher.delete_teacher(teacher_id)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif teacher_choice == "4":
                    try:
                        teacher_id = int(input("Enter teacher ID to get details: "))
                        teacher = Teacher.get_teacher(teacher_id)
                        if teacher:
                            print(f"Teacher ID: {teacher[0]}")
                            print(f"Name: {teacher[1]}")
                            print(f"Contact Number: {teacher[2]}")
                            print(f"Subject Taught: {teacher[3]}")
                        else:
                            print("Teacher not found.")
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif teacher_choice == "5":
                    teachers = Teacher.get_all_teachers()
                    if teachers:
                        headers = ["Teacher ID", "Name", "Contact Number", "Subject Taught"]
                        data = [[t[0], t[1], t[2], t[3]] for t in teachers]
                        print(tabulate(data, headers=headers, tablefmt="grid"))
                    else:
                        print("No teachers found.")
                elif teacher_choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            while True:
                print(" Course Management ".center(50, "="))
                print("1. Add Course")
                print("2. Update Course")
                print("3. Delete Course")
                print("4. Get Course")
                print("5. Get all Courses")
                print("6. Exit")
                course_choice = input("Enter your choice: ")

                if course_choice == "1":
                    try:
                        course_id = int(input("Enter course ID: "))
                        name = input("Enter course name: ")
                        teacher_id = int(input("Enter teacher ID: "))
                        maximum_students = int(input("Enter maximum number of students: "))
                        Course.add_course(course_id, name, teacher_id, maximum_students)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif course_choice == "2":
                    try:
                        course_id = int(input("Enter course ID to update: "))
                        name = input("Enter course name (leave blank to skip): ")
                        teacher_id = input("Enter teacher ID (leave blank to skip): ")
                        teacher_id = int(teacher_id) if teacher_id else None
                        maximum_students = input("Enter maximum number of students (leave blank to skip): ")
                        maximum_students = int(maximum_students) if maximum_students else None
                        Course.update_course(course_id, name, teacher_id, maximum_students)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif course_choice == "3":
                    try:
                        course_id = int(input("Enter course ID to delete: "))
                        Course.delete_course(course_id)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif course_choice == "4":
                    try:
                        course_id = int(input("Enter course ID to get details: "))
                        course = Course.get_course(course_id)
                        if course:
                            print(f"Course ID: {course[0]}")
                            print(f"Name: {course[1]}")
                            print(f"Teacher ID: {course[2]}")
                            print(f"Maximum Students: {course[3]}")
                        else:
                            print("Course not found.")
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif course_choice == "5":
                    courses = Course.get_all_courses()
                    if courses:
                        headers = ["Course ID", "Name", "Teacher ID", "Maximum Students"]
                        data = [[c[0], c[1], c[2], c[3]] for c in courses]
                        print(tabulate(data, headers=headers, tablefmt="grid"))
                    else:
                        print("No courses found.")
                elif course_choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4":
            while True:
                print(" Grade Management ".center(50, "="))
                print("1. Add Grade")
                print("2. Get Grades for Student")
                print("3. Exit")
                grade_choice = input("Enter your choice: ")

                if grade_choice == "1":
                    try:
                        grade_id = int(input("Enter grade ID: "))
                        student_id = int(input("Enter student ID: "))
                        course_id = int(input("Enter course ID: "))
                        grade = input("Enter grade: ")
                        Grade.add_grade(grade_id, student_id, course_id, grade)
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif grade_choice == "2":
                    try:
                        student_id = int(input("Enter student ID to get grades: "))
                        grades = Grade.get_grades_for_student(student_id)
                        if grades:
                            headers = ["Grade ID", "Student ID", "Course ID", "Grade"]
                            data = [[g[0], g[1], g[2], g[3]] for g in grades]
                            print(tabulate(data, headers=headers, tablefmt="grid"))
                        else:
                            print("No grades found for the student.")
                    except ValueError:
                        print("Invalid input. Please try again.")
                elif grade_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
