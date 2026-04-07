# Menu-based program
students = {}

while True:
    print("\nMenu:")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added!")

    elif choice == "B":
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated!")
        else:
            print("Student not found!")

    elif choice == "C":
        name = input("Enter student name to search: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Student not found!")

    elif choice == "D":
        if students:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(name, ":", marks)
        else:
            print("No records found!")

    elif choice == "E":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")