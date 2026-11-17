import tkinter as tk
from datetime import datetime

def course_enrollment(student_id, first_name, last_name, course_id, course_name, action="Echo"):
    print(f"\nAction: {action}")
    print(f"Student ID: {student_id}")
    print(f"Student Name: {first_name} {last_name}")
    print(f"Course ID: {course_id}")
    print(f"Course Name: {course_name}")
    print(f"Enrollment action: {action}")


def exercise_1():
    print("\n--- Student Registration ---")

    
    course_enrollment(1001, "Alice", "Smith", "ICT105", "Programming Principles")

    course_enrollment(1002, "Bob", "Johnson", "ICT104",
                      "Data Communication", action="Add")

    course_enrollment(1001, "Alice", "Smith", "ICT105",
                      "Programming Principles", action="Amend")

    course_enrollment(1002, "Bob", "Johnson", "ICT104",
                      "Data Communication", action="Delete")


def collect_courses():
    courses = []

    for i in range(4):
        course_id = input(f"Enter course ID {i + 1}: ").strip()
        courses.append(course_id)

    return courses


def store_course_details(**courses):
    return courses


def student_course_list(student_id, student_name):
    print(f"\nStudent ID: {student_id}")
    print(f"Student Name: {student_name}")

    courses = collect_courses()

    print("\nEnrolled Courses:")
    for course in courses:
        print(course)

    semester = input("\nEnter semester (S1/S2): ")
    year = input("Enter year: ")

    print(f"\nSemester: {semester}")
    print(f"Year: {year}")

    return courses


def exercise_2():
    print("\n--- Student Course List ---")

    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")

    enrolled_courses = student_course_list(student_id, student_name)

    course_details = store_course_details(
        ICT105="Programming Principles",
        ICT104="Data Communication",
        BUS103="Management Functions",
        BUS105="Business Information Systems"
    )

    print("\nCourse Information:")
    for course_id in enrolled_courses:
        course_name = course_details.get(course_id.upper(), "Unknown Course")
        print(f"{course_id.upper()}: {course_name}")

def exercise_3():
    root = tk.Tk()
    root.title("Basic Calculator")
    root.geometry("350x300")

    tk.Label(root, text="First Number:").pack(pady=5)
    first_entry = tk.Entry(root, width=20)
    first_entry.pack()

    tk.Label(root, text="Second Number:").pack(pady=5)
    second_entry = tk.Entry(root, width=20)
    second_entry.pack()

    result_label = tk.Label(root, text="Result:", font=("Arial", 12))
    result_label.pack(pady=15)

    def calculate(operation):
        try:
            num1 = float(first_entry.get())
            num2 = float(second_entry.get())

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    result_label.config(text="Cannot divide by zero")
                    return
                result = num1 / num2

            result_label.config(text=f"Result: {result}")

        except ValueError:
            result_label.config(text="Please enter valid numbers")

    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    tk.Button(button_frame, text="+", width=5,
              command=lambda: calculate("+")).grid(row=0, column=0, padx=3)

    tk.Button(button_frame, text="-", width=5,
              command=lambda: calculate("-")).grid(row=0, column=1, padx=3)

    tk.Button(button_frame, text="*", width=5,
              command=lambda: calculate("*")).grid(row=0, column=2, padx=3)

    tk.Button(button_frame, text="/", width=5,
              command=lambda: calculate("/")).grid(row=0, column=3, padx=3)

    root.mainloop()

class User:
    def __init__(self, first_name, last_name, email, username,
                 date_of_birth, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Welcome, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


def exercise_4():
    print("\n--- User Profiles ---")

    user1 = User("Alice", "Smith", "alice@email.com",
                 "alice01", "2003-05-12", "Perth")

    user2 = User("Bob", "Johnson", "bob@email.com",
                 "bob02", "2002-08-20", "Sydney")

    user3 = User("Charlie", "Brown", "charlie@email.com",
                 "charlie03", "2004-03-15", "Melbourne")

    users = [user1, user2, user3]

    for user in users:
        user.describe_user()
        user.greet_user()


def exercise_5():
    print("\n--- Login Attempts ---")

    user = User("Alice", "Smith", "alice@email.com",
                "alice01", "2003-05-12", "Perth")

    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()

    print(f"Login attempts: {user.login_attempts}")

    user.reset_login_attempts()

    print(f"Login attempts after reset: {user.login_attempts}")


class classroom:
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class
        self.students_enrolled = 0
        self.audit_log = []

    def describe_classroom(self):
        print(f"\nClassroom: {self.classroom_name}")
        print(f"Location: {self.classroom_location}")
        print(f"Seats Available: {self.seats_in_class}")

    def checksize_classroom(self):
        if self.students_enrolled <= self.seats_in_class:
            print("The classroom has enough seats for the enrolled students.")
        else:
            print("The classroom does not have enough seats.")

    def record_change(self, old_value, new_value):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.audit_log.append({
            "time": time,
            "old_value": old_value,
            "new_value": new_value
        })

    def set_number_enrolled(self, number):
        if number < 0:
            print("Student count cannot be negative.")
            return

        old_value = self.students_enrolled
        self.students_enrolled = number
        self.record_change(old_value, number)

    def update_number_enrolled(self, number):
        if number < 0:
            print("Student count cannot be negative.")
            return

        old_value = self.students_enrolled
        self.students_enrolled += number

        if self.students_enrolled < 0:
            self.students_enrolled = old_value
            print("Student count cannot be negative.")
            return

        self.record_change(old_value, self.students_enrolled)

    def show_audit_log(self):
        print("\n--- Enrollment Audit Log ---")

        for log in self.audit_log:
            print(f"Date: {log['time']}")
            print(f"Previous Students: {log['old_value']}")
            print(f"Updated Students: {log['new_value']}")
            print()


def exercise_6():
    print("\n--- Classroom Information ---")

    classroom1 = classroom("Room 101", "Building A", 30)
    classroom2 = classroom("Room 102", "Building A", 25)
    classroom3 = classroom("Room 201", "Building B", 40)

    print(classroom1.classroom_name)
    print(classroom1.classroom_location)
    print(classroom1.seats_in_class)

    classroom1.describe_classroom()
    classroom1.checksize_classroom()

    for room in [classroom1, classroom2, classroom3]:
        room.describe_classroom()


def exercise_7():
    print("\n--- Enrolled Students ---")

    room = classroom("Room 101", "Building A", 30)

    print(f"Initial Students: {room.students_enrolled}")

    old_value = room.students_enrolled
    room.students_enrolled = 10
    room.record_change(old_value, room.students_enrolled)

    print(f"Updated Students: {room.students_enrolled}")

    room.set_number_enrolled(20)
    print(f"Students after setting: {room.students_enrolled}")

    room.update_number_enrolled(5)
    print(f"Students after update: {room.students_enrolled}")

    room.checksize_classroom()
    room.show_audit_log()


class equipment(classroom):
    def __init__(self, classroom_name, classroom_location,
                 seats_in_class, devices):
        super().__init__(classroom_name, classroom_location, seats_in_class)
        self.devices = devices

    def display_devices(self):
        print(f"\nEquipment in {self.classroom_name}:")

        for device in self.devices:
            print(f"- {device}")


def exercise_8():
    print("\n--- Classroom Equipment ---")

    devices = [
        "Interactive Whiteboard",
        "Desktop Computers",
        "Laptops",
        "Tablets",
        "Document Camera",
        "Smart TV",
        "Sound System",
        "Wi-Fi Access Point",
        "Charging Station",
        "Digital Signage"
    ]

    room_equipment = equipment("Room 101", "Building A", 30, devices)

    room_equipment.describe_classroom()
    room_equipment.display_devices()


def main():
    while True:
        print("\n================================")
        print("ICT105 - Worksheet 4")
        print("Sessions 7 & 8")
        print("================================")
        print("1. Student Registration")
        print("2. Student Course List")
        print("3. Tkinter Calculator")
        print("4. User Profile")
        print("5. Login Attempts")
        print("6. Classroom Information")
        print("7. Enrolled Students")
        print("8. Classroom Equipment")
        print("9. Exit")

        choice = input("\nChoose an exercise (1-9): ").strip()

        if choice == "1":
            exercise_1()
        elif choice == "2":
            exercise_2()
        elif choice == "3":
            exercise_3()
        elif choice == "4":
            exercise_4()
        elif choice == "5":
            exercise_5()
        elif choice == "6":
            exercise_6()
        elif choice == "7":
            exercise_7()
        elif choice == "8":
            exercise_8()
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
