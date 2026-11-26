# Name: Mariella Ovido
# Section: IV-BSIT
# Activity: P2 - Main Program
# Date: November 18, 2026

import student_utils
from student_utils import get_status
from datetime import datetime

print("================================")
print("Student: Mariella Ovido")
print("Section: IV-BSIT C")
print("================================")

grades = []

while True:
    try:
        count = int(input("How many grades do you want to enter? "))

        if count > 0:
            break

        print("Please enter a positive number.")

    except ValueError:
        print("Invalid input. Enter a number only.")

for i in range(count):
    while True:
        try:
            grade = float(input(f"Enter grade #{i + 1}: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break

            print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid grade.")

print("\n===== STUDENT REPORT =====")

print("Report Generated:")
print(datetime.now())

print(f"\nAverage Grade : {student_utils.calculate_average(grades):.2f}")
print(f"Highest Grade : {student_utils.get_highest(grades)}")
print(f"Lowest Grade  : {student_utils.get_lowest(grades)}")
print(f"Status        : {get_status(grades)}")
