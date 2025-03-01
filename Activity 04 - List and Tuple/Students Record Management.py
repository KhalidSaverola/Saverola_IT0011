import json

file_name = "students.json"

students = []

def save_file():
    with open(file_name, "w") as file:
        json.dump(students, file)
    print("Records saved successfully!")

def open_file():
    global students
    try:
        with open(file_name, "r") as file:
            students[:] = json.load(file)
        print("Records loaded successfully!")
    except FileNotFoundError:
        print("No existing file found.")

def show_all_records():
    print("\nStudent Records:")
    for student in students:
        print(student)

def order_by_last_name():
    sorted_students = sorted(students, key=lambda x: x[1][1])
    print("\nStudents Ordered by Last Name:")
    for student in sorted_students:
        print(student)

def order_by_grade():
    sorted_students = sorted(students, key=lambda x: (x[2] * 0.6) + (x[3] * 0.4), reverse=True)
    print("\nStudents Ordered by Grade:")
    for student in sorted_students:
        print(student)

def show_student_record():
    student_id = input("Enter Student ID: ")
    for student in students:
        if student[0] == student_id:
            print("\nStudent Record:", student)
            return
    print("Student not found.")

def add_record():
    student_id = input("Enter Student ID (6 digits): ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added successfully!")

def edit_record():
    student_id = input("Enter Student ID to Edit: ")
    for i, student in enumerate(students):
        if student[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully!")
            return
    print("Student not found.")

def delete_record():
    student_id = input("Enter Student ID to Delete: ")
    global students
    students = [student for student in students if student[0] != student_id]
    print("Record deleted successfully!")

def menu():
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Show All Students Record")
        print("4. Order by Last Name")
        print("5. Order by Grade")
        print("6. Show Student Record")
        print("7. Add Record")
        print("8. Edit Record")
        print("9. Delete Record")
        print("10. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            open_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            show_all_records()
        elif choice == "4":
            order_by_last_name()
        elif choice == "5":
            order_by_grade()
        elif choice == "6":
            show_student_record()
        elif choice == "7":
            add_record()
        elif choice == "8":
            edit_record()
        elif choice == "9":
            delete_record()
        elif choice == "10":
            break
        else:
            print("Invalid choice, please try again.")


menu()
