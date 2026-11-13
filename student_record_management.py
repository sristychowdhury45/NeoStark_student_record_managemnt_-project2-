
import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read student records.")
            return []
    return []



def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
        return True
    except OSError:
        print("Error: Unable to save student records.")
        return False



def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if any(s["id"] == student_id for s in students):
        print("Error: Student ID already exists!")
        return

    name = input("Student Name: ").strip()
    department = input("Department: ").strip()

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    try:
        marks = [float(x.strip()) for x in input(
            "Enter Marks (comma separated): "
        ).split(",")]

        if not marks or any(m < 0 or m > 100 for m in marks):
            print("Invalid marks! Enter marks between 0 and 100.")
            return

        attendance = float(input("Attendance (%): "))

        if not 0 <= attendance <= 100:
            print("Attendance must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    student = {
        "id": student_id,
        "name": name,
        "department": department,
        "marks": marks,
        "attendance": attendance
    }

    students.append(student)

    if save_students(students):
        print("\nStudent added successfully!")



def view_students(students):
    if not students:
        print("\nNo student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for s in students:
        average = sum(s["marks"]) / len(s["marks"])

        print("\nStudent ID:", s["id"])
        print("Name:", s["name"])
        print("Department:", s["department"])
        print("Marks:", s["marks"])
        print("Average: {:.2f}%".format(average))
        print("Attendance: {}%".format(s["attendance"]))



def search_student(students):
    student_id = input("Enter Student ID to search: ").strip()

    for s in students:
        if s["id"] == student_id:
            average = sum(s["marks"]) / len(s["marks"])

            print("\nStudent Found")
            print("----------------------")
            print("Student ID:", s["id"])
            print("Name:", s["name"])
            print("Department:", s["department"])
            print("Average: {:.2f}%".format(average))
            print("Attendance: {}%".format(s["attendance"]))
            return

    print("Student record not found.")



def update_student(students):
    student_id = input("Enter Student ID to update: ").strip()

    for s in students:
        if s["id"] == student_id:
            print("Student Found. Enter new details.")

            name = input("New Name (press Enter to keep old): ").strip()
            department = input(
                "New Department (press Enter to keep old): "
            ).strip()

            try:
                marks_input = input(
                    "New Marks (comma separated, Enter to keep old): "
                ).strip()

                if marks_input:
                    new_marks = [
                        float(x.strip()) for x in marks_input.split(",")
                    ]

                    if not new_marks or any(
                        m < 0 or m > 100 for m in new_marks
                    ):
                        print("Invalid marks!")
                        return

                    s["marks"] = new_marks

                attendance_input = input(
                    "New Attendance (Enter to keep old): "
                ).strip()

                if attendance_input:
                    attendance = float(attendance_input)

                    if not 0 <= attendance <= 100:
                        print("Invalid attendance!")
                        return

                    s["attendance"] = attendance

            except ValueError:
                print("Invalid input!")
                return

            if name:
                s["name"] = name

            if department:
                s["department"] = department

            if save_students(students):
                print("Student updated successfully!")
            return

    print("Student record not found.")


# Delete student
def delete_student(students):
    student_id = input("Enter Student ID to delete: ").strip()

    for s in students:
        if s["id"] == student_id:
            students.remove(s)

            if save_students(students):
                print("Student deleted successfully!")
            return

    print("Student record not found.")


# Calculate student performance
def performance_report(students):
    if not students:
        print("No student records available.")
        return

    print("\n========== PERFORMANCE REPORT ==========")

    for s in students:
        average = sum(s["marks"]) / len(s["marks"])

        if average >= 90:
            grade = "A+"
            performance = "Excellent"
        elif average >= 80:
            grade = "A"
            performance = "Very Good"
        elif average >= 70:
            grade = "B"
            performance = "Good"
        elif average >= 60:
            grade = "C"
            performance = "Average"
        elif average >= 40:
            grade = "D"
            performance = "Pass"
        else:
            grade = "F"
            performance = "Fail"

        print("\nName:", s["name"])
        print("Average: {:.2f}%".format(average))
        print("Grade:", grade)
        print("Performance:", performance)
        print("Attendance: {}%".format(s["attendance"]))



def main():
    students = load_students()

    print("========================================")
    print("     STUDENT RECORD MANAGEMENT SYSTEM")
    print("========================================")
    print("Student records loaded:", len(students))

    while True:
        print("\nChoose an option:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Performance Report")
        print("7. Save Records")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            performance_report(students)

        elif choice == "7":
            if save_students(students):
                print("Records saved successfully!")

        elif choice == "8":
            if save_students(students):
                print("Records saved successfully!")
                print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Please select 1 to 8.")


if __name__ == "__main__":
    main()
