# Name: Mariella Ovido
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 18, 2026

students = []


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    for student in students:
        if student.lower() == name.lower():
            print("Student already exists.")
            return

    students.append(name)
    print("Student added successfully.")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print("Student removed successfully.")
            return

    print("Student not found.")


def search_student():
    keyword = input("Enter name to search: ").strip().lower()

    found = False

    print("\nSearch Results:")

    for student in students:
        if keyword in student.lower():
            print(student)
            found = True

    if not found:
        print("No matching student found.")


def display_students():
    if len(students) == 0:
        print("\nNo student records available.")
        return

    print("\n===== STUDENT LIST =====")

    for index, student in enumerate(students, start=1):
        print(f"{index}. {student}")

    print(f"\nTotal Students: {len(students)}")


def main():
    print("================================")
    print("Student: Mariella Ovido")
    print("Section: IV-BSIT C")
    print("================================")

    while True:
        print("\n===== MENU =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please try again.")


main()
