# ==========================================
# STUDENT INFORMATION MANAGEMENT SYSTEM
# ==========================================

# Dictionary to store student records
students = {}


# ------------------------------------------
# Function to Add Student
# ------------------------------------------
def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    students[roll] = {
        "name": name,
        "age": age,
        "marks": marks
    }

    print("Student record added successfully!")


# ------------------------------------------
# Function to View All Students
# ------------------------------------------
def view_students():

    if not students:
        print("No student records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for roll, info in students.items():

        print("\n----------------------------")
        print(f"Roll Number : {roll}")
        print(f"Name        : {info['name']}")
        print(f"Age         : {info['age']}")
        print(f"Marks       : {info['marks']}")
        print("----------------------------")


# ------------------------------------------
# Function to Search Student
# ------------------------------------------
def search_student():

    roll = input("Enter Roll Number to search: ")

    if roll in students:

        print("\nStudent Found!")
        print(f"Name  : {students[roll]['name']}")
        print(f"Age   : {students[roll]['age']}")
        print(f"Marks : {students[roll]['marks']}")

    else:
        print("Student not found.")


# ------------------------------------------
# Function to Update Student
# ------------------------------------------
def update_student():

    roll = input("Enter Roll Number to update: ")

    if roll in students:

        print("\nEnter New Details")

        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        marks = input("Enter New Marks: ")

        students[roll] = {
            "name": name,
            "age": age,
            "marks": marks
        }

        print("Student record updated successfully!")

    else:
        print("Student not found.")


# ------------------------------------------
# Function to Delete Student
# ------------------------------------------
def delete_student():

    roll = input("Enter Roll Number to delete: ")

    if roll in students:

        del students[roll]
        print("Student record deleted successfully!")

    else:
        print("Student not found.")


# ==========================================
# Main Program
# ==========================================
while True:

    print("\n===================================")
    print("  STUDENT INFORMATION MANAGEMENT")
    print("===================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # Menu Selection
    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nExiting Information Management System...")
        break

    else:
        print("Invalid choice! Please try again.")