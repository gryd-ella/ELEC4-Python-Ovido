# Name: Mariella Ovido
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 18, 2026


def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print(f"Result: {result}")

    finally:
        print("Division operation completed.\n")


def open_file():
    try:
        filename = input("Enter filename: ")

        file = open(filename, "r")

    except FileNotFoundError:
        print("Error: File not found.")

    else:
        print("\nFile Contents:")
        print(file.read())
        file.close()

    finally:
        print("File operation completed.\n")


def main():
    print("================================")
    print("Student: Mariella Ovido")
    print("Section: IV-BSIT C")
    print("================================")

    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("1. Divide Numbers")
        print("2. Open File")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                divide_numbers()

            elif choice == 2:
                open_file()

            elif choice == 3:
                print("Program terminated.")
                break

            else:
                print("Invalid menu option.")

        except ValueError:
            print("Please enter a valid number only.")


main()
