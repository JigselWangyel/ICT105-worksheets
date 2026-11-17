courses = [
    "Introduction to Programming",
    "Calculus I",
    "Data Structures and Algorithms",
    "Linear Algebra",
    "Physics I",
    "Chemistry I",
    "Biology I",
    "Microeconomics",
    "Macroeconomics",
    "Psychology I",
    "History I",
    "English Composition I",
    "Introduction to Philosophy",
    "Calculus II",
    "Discrete Mathematics"
]

print ("\n")

print(courses)
print ("\n")
 

print("Original list:", courses)
print ("\n")


print("Alphabetical order:", sorted(courses))
print ("\n")

print("Reverse alphabetical:", sorted(courses, reverse=True))
print ("\n")


courses.reverse()
print("Reversed list:", courses)
print ("\n")


courses.reverse()
print("Original order restored:", courses)
print ("\n")


courses.sort()
print("Permanently sorted:", courses)
print ("\n")


courses.sort(reverse=True)
print("Permanently sorted in reverse:", courses)
print ("\n")

available_courses = sorted(courses)

print("\n AVAILABLE COURSES")

print("The following courses are available for expression of interest")
print("if students meet the prerequisites:\n")

for course in available_courses:
    print(course)
print ("\n")
    

old_course = "Physics I"
new_course = "Discrete Mathematics"

available_courses.remove(old_course)

available_courses.append(new_course)

print("\n COURSE REPLACEMENT")

print("Withdrawn course:", old_course)
print("Replacement course:", new_course)

print("\nUpdated courses:")

for course in available_courses:
    print(course)


available_courses.insert(0, "Linear Algebra")

available_courses.insert(3, "Calculus II")

available_courses.append("Data Structures and Algorithms")


print("\n NEW COURSES ADDED")

for course in available_courses:
    print(course)


print("\n WITHDRAWN COURSES")

withdrawn1 = available_courses.pop(0)
withdrawn2 = available_courses.pop(1)
withdrawn3 = available_courses.pop(2)
withdrawn4 = available_courses.pop(3)


print("Withdrawn:", withdrawn1)
print("Withdrawn:", withdrawn2)
print("Withdrawn:", withdrawn3)
print("Withdrawn:", withdrawn4)

print("\nWithdrawal of four courses confirmed.")


print("\n REMAINING COURSES")

for course in available_courses:
    print(course)

course_data = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I"),
    (11, "History I"),
    (12, "English Composition I"),
    (13, "Introduction to Philosophy"),
    (14, "Calculus II"),
    (15, "Discrete Mathematics")
]



course_information = []


for course_id, course_name in course_data:
    
    course_information.append((course_id, course_name))



print("\n COURSE INFORMATION")

for course_id, course_name in course_information:

    print("Course ID:", course_id)
    print("Course Name:", course_name)
    print("\n")
   

course_information = []

for course_id, course_name in course_data:
    course_information.append((course_name))
    
    
departments = [
    (1, "Computer Science"),
    (2, "Mathematics"),
    (3, "Computer Science"),
    (4, "Mathematics"),
    (5, "Physics"),
    (6, "Chemistry"),
    (7, "Biology"),
    (8, "Economics"),
    (9, "Economics"),
    (10, "Psychology"),
    (11, "History"),
    (12, "English"),
    (13, "Philosophy"),
    (14, "Mathematics"),
    (15, "Computer Science")
]


print("\n DEPARTMENT SEARCH")

while True:
    
    user_input = input("\nEnter Course ID (1-15) or quit/0: ")
    
    if user_input.lower() == "quit" or user_input == "0":
    
        print("The value", user_input, "has been used to exit.")
        break
    
    
    elif user_input.isdigit():
    
        course_id = int(user_input)
        found = False

        for id, department in departments:
            if course_id == id:
        
                print("Course ID", course_id, "is in the", department, "department.")

                found = True
                break

        if not found:

            print("Course ID is out of range (1-15), try again.")
            
    else:
    
     print("Invalid input. Please enter a number from 1 to 15.")
     

course_details = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconom"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science", "Introduction"]
]

print("\n========== COURSE INFORMATION RETRIEVAL ==========")

while True:

    user_input = input(
        "\nEnter Course ID (1-15) or 0/quit to exit: "
    )

    if user_input.lower() == "quit" or user_input == "0":

        print("Exiting course information system.")
        break

    elif not user_input.isdigit():

        print("Invalid input. Please enter a number.")
        continue

    else:

        search_id = int(user_input)

        found = False

        for course in course_details:

            if course[0] == search_id:

                print("\n========== COURSE FOUND ==========")

                print("Course ID:", course[0])
                print("Course Name:", course[1])
                print("Department:", course[2])
                print("Prerequisites:", course[3])

                found = True
                break

        if not found:

            print("Course ID not found. Please try again.")
