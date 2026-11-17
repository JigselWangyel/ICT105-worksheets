
import csv
import json
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

API_URL = "https://api.github.com/search/repositories?q=language:python+sort:stars"


class PythonLearning:
    def __init__(self, filename):
        self.filename = BASE_DIR / filename

    def create_file(self):
        content = [
            "Python is a programming language.\n",
            "I learned about variables, lists and dictionaries.\n",
            "Functions help organise code.\n",
            "Classes and objects are used in OOP.\n",
            "Error handling helps prevent program crashes.\n"
        ]

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.writelines(content)

            print("File created successfully.")

        except PermissionError:
            print("Permission denied when creating the file.")
        except OSError as error:
            print(f"File error: {error}")

    def read_all(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                print("\nFull File Content:")
                print(file.read())

        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")

    def read_lines(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()

            print("\nReading Line by Line:")
            for line in lines:
                print(line.strip())

        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")


def exercise_1():
    print("\n--- Reading Files ---")

    learning = PythonLearning("learning_python.txt")

    learning.create_file()
    learning.read_all()
    learning.read_lines()



def exercise_2():
    print("\n--- Replacing Words ---")

    filename = BASE_DIR / "learning_students.txt"

    content = [
        "Every learner must complete their assignments on time.\n",
        "A good learner always seeks to learn more.\n",
        "Learners are the future leaders.\n"
    ]

    try:
    
        if not filename.exists():
            with open(filename, "w", encoding="utf-8") as file:
                file.writelines(content)

      
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                modified = line.replace("learner", "student")
                modified = modified.replace("Learners", "Students")
                print(modified.strip())

    except FileNotFoundError:
        print("The file could not be found.")
    except PermissionError:
        print("Permission denied.")
    except OSError as error:
        print(f"File error: {error}")



def exercise_3():
    print("\n--- Adding Two Numbers ---")

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        total = num1 + num2

        print(f"The total is: {total}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


def exercise_4():
    print("\n--- Calculator ---")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))

            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            operation = input("Choose operation (1-4): ")

            if operation == "1":
                result = num1 + num2
            elif operation == "2":
                result = num1 - num2
            elif operation == "3":
                result = num1 * num2
            elif operation == "4":
                if num2 == 0:
                    print("Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Please enter valid numeric values.")

        again = input("\nCalculate again? (yes/no): ").lower()

        if again not in ("yes", "y"):
            break

def split_students_csv():
    source = BASE_DIR / "students.csv"

    try:
        with open(source, "r", newline="", encoding="utf-8-sig") as file:
            rows = list(csv.reader(file))

        if not rows:
            print("The CSV file is empty.")
            return False

    
        if rows[0][0].lower() in ("studentid", "student_id"):
            header = rows[0]
            students = rows[1:]
        else:
            header = None
            students = rows

        middle = (len(students) + 1) // 2

        first_half = students[:middle]
        second_half = students[middle:]

        files = [
            ("students_c1.txt", first_half),
            ("students_c2.txt", second_half)
        ]

        for filename, data in files:
            with open(BASE_DIR / filename, "w",
                      newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                if header:
                    writer.writerow(header)

                writer.writerows(data)

        print("Student data split into two files.")
        return True

    except FileNotFoundError:
        print("students.csv was not found.")
        return False
    except PermissionError:
        print("Permission denied.")
        return False
    except OSError as error:
        print(f"File error: {error}")
        return False


def read_student_files(silent=False):
    filenames = ["students_c1.txt", "students_c2.txt"]

    if silent:
        logging.basicConfig(
            filename=str(BASE_DIR / "error.log"),
            level=logging.ERROR,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    for filename in filenames:
        try:
            with open(BASE_DIR / filename, "r",
                      encoding="utf-8") as file:
                content = file.read()

            print(f"\n--- {filename} ---")
            print(content)

        except FileNotFoundError:
            if silent:
                logging.error(f"Missing file: {filename}")
            else:
                print(f"File not found: {filename}")

        except PermissionError:
            if silent:
                logging.error(f"Permission denied: {filename}")
            else:
                print(f"Permission denied: {filename}")


def exercise_5():
    print("\n--- Student CSV Files ---")

    print("1. Split students.csv into two files")
    print("2. Read student files with error messages")
    print("3. Read student files with silent error logging")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        split_students_csv()
    elif choice == "2":
        read_student_files()
    elif choice == "3":
        read_student_files(silent=True)
    else:
        print("Invalid choice.")



def exercise_6():
    print("\n--- Favourite Number ---")

    filename = BASE_DIR / "favorite_number.json"

    try:
        number = int(input("Enter your favourite number: "))

        with open(filename, "w", encoding="utf-8") as file:
            file.write(json.dumps(number))

    
        with open(filename, "r", encoding="utf-8") as file:
            saved_number = json.loads(file.read())

        print(f"Your favourite number is {saved_number}.")

    except ValueError:
        print("Please enter a valid number.")
    except (OSError, json.JSONDecodeError) as error:
        print(f"File error: {error}")



def get_favourite_number():
    filename = BASE_DIR / "remember_number.json"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            number = json.load(file)
            return number

    except (FileNotFoundError, json.JSONDecodeError):
        return None


def save_favourite_number(number):
    filename = BASE_DIR / "remember_number.json"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(number, file)

        print("Favourite number saved successfully.")

    except OSError as error:
        print(f"Could not save number: {error}")


def exercise_7():
    print("\n--- Remember Favourite Number ---")

    number = get_favourite_number()

    if number is not None:
        print(f"I remember your favourite number! It is {number}.")

    else:
        try:
            number = int(input("Enter your favourite number: "))
            save_favourite_number(number)

        except ValueError:
            print("Please enter a valid number.")



def exercise_8():
    print("\n--- Student User Profile ---")

    filename = BASE_DIR / "user_profile.txt"


    try:
        with open(filename, "r", encoding="utf-8") as file:
            profiles = json.load(file)

        if not isinstance(profiles, dict):
            profiles = {}

    except (FileNotFoundError, json.JSONDecodeError):
        profiles = {}

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id not in profiles:
        profiles[student_id] = {
            "student_id": student_id
        }

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(profiles, file, indent=4)

        
        with open(filename, "r", encoding="utf-8") as file:
            profiles = json.load(file)

        dob = input("Enter date of birth (DD/MM/YYYY): ")
        email = input("Enter email address: ")

        profiles[student_id]["date_of_birth"] = dob
        profiles[student_id]["email"] = email

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(profiles, file, indent=4)

        print("\n--- Student Profile Report ---")

        with open(filename, "r", encoding="utf-8") as file:
            saved_profiles = json.load(file)

        for student, details in saved_profiles.items():
            print(f"\nStudent ID: {student}")
            print(f"Date of Birth: {details.get('date_of_birth', 'Not entered')}")
            print(f"Email: {details.get('email', 'Not entered')}")

    except (OSError, json.JSONDecodeError) as error:
        print(f"Profile file error: {error}")



def exercise_9():
    print("\n--- Remember Me ---")

    filename = BASE_DIR / "username.json"

    usernames = []
    last_user = None

    try:
        with open(filename, "r", encoding="utf-8") as file:
            saved_data = json.load(file)

        if isinstance(saved_data, dict):
            usernames = saved_data.get("usernames", [])
            last_user = saved_data.get("last_user")

            if "username" in saved_data:
                old_name = saved_data["username"]

                if old_name not in usernames:
                    usernames.append(old_name)

                if last_user is None:
                    last_user = old_name

    except (FileNotFoundError, json.JSONDecodeError):
        pass

    if last_user:
        print(f"Last saved user: {last_user}")
        answer = input("Is this you? (yes/no): ").lower().strip()

        if answer in ("yes", "y"):
            username = last_user
        else:
            username = input("Enter a new username: ").strip()
    else:
        username = input("Enter your username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if username in usernames:
        print("This username already exists.")
    else:
        usernames.append(username)

    data = {
        "last_user": username,
        "usernames": usernames
    }

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Username '{username}' saved or updated successfully.")

    except OSError as error:
        print(f"Unable to save username: {error}")



def get_github_repositories():
    try:
        import requests

    except ImportError:
        print("Please install requests first.")
        print("Run: python -m pip install requests")
        return None, None

    try:
        response = requests.get(
            API_URL,
            timeout=15,
            headers={"Accept": "application/vnd.github+json"}
        )

        if response.status_code != 200:
            print(f"GitHub request failed. Status: {response.status_code}")
            return None, response.headers

        return response.json(), response.headers

    except requests.RequestException as error:
        print(f"API request error: {error}")
        return None, None

    except ValueError:
        print("Invalid JSON response.")
        return None, None


def exercise_10():
    print("\n--- GitHub API ---")

    data, headers = get_github_repositories()

    if data is None:
        return

    print("\nTop 5 Python Repositories:")

    repositories = data.get("items", [])[:5]

    for index, repo in enumerate(repositories, start=1):
        print(f"{index}. {repo.get('full_name', 'Unknown')}")


def exercise_11():
    print("\n--- Virtual Environment Commands ---")

    print("\nCreate a virtual environment:")
    print("python -m venv .venv")

    print("\nActivate on Windows PowerShell:")
    print(r".\.venv\Scripts\Activate.ps1")

    print("\nActivate on macOS/Linux:")
    print("source .venv/bin/activate")

    print("\nExport installed packages:")
    print("python -m pip freeze > requirements.txt")

    print("\nInstall packages from requirements.txt:")
    print("python -m pip install -r requirements.txt")



def exercise_12():
    print("\n--- API Response Dictionary ---")

    data, headers = get_github_repositories()

    if data is None:
        print("Unable to retrieve repository information.")
        return

    total_count = data.get("total_count", 0)

    print(f"Total Python repositories found: {total_count}")

    if data.get("incomplete_results"):
        print("GitHub reports that the search results are incomplete.")


def exercise_13():
    print("\n--- GitHub Repository Chart ---")

    try:
        import plotly.express as px

    except ImportError:
        print("Please install Plotly first.")
        print("Run: python -m pip install plotly")
        return

    data, headers = get_github_repositories()

    if data is None:
        return

   
    if headers:
        remaining = headers.get("X-RateLimit-Remaining", "Unknown")
        reset = headers.get("X-RateLimit-Reset", "Unknown")

        print(f"\nAPI requests remaining: {remaining}")
        print(f"Rate limit reset: {reset}")

        if remaining == "0":
            print("API limit reached. Try again after the reset time.")

    repositories = data.get("items", [])[:10]

    if not repositories:
        print("No repository data available.")
        return

    repo_names = []
    stars = []

    for repo in repositories:
        repo_names.append(repo.get("name", "Unknown"))
        stars.append(repo.get("stargazers_count", 0))

    fig = px.bar(
        x=repo_names,
        y=stars,
        title="Top 10 Python GitHub Repositories",
        labels={
            "x": "Repository Names",
            "y": "Number of Stars"
        }
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    try:
        fig.show()
        print("Repository chart displayed.")

    except Exception as error:
        print(f"Could not display the chart: {error}")



def main():
    while True:
        print("\n====================================")
        print("ICT105 - WORKSHEET 5")
        print("Sessions 9 & 10")
        print("====================================")

        print("\nSESSION 9 - Error Handling")
        print("1. Reading Files")
        print("2. Replacing Words")
        print("3. Numeric Error Handling")
        print("4. Repeatable Calculator")
        print("5. Student CSV Files")
        print("6. Favourite Number")
        print("7. Remember Favourite Number")
        print("8. Student User Profile")
        print("9. Remember Username")

        print("\nSESSION 10 - Working with APIs")
        print("10. GitHub API")
        print("11. Virtual Environment")
        print("12. API Response Dictionary")
        print("13. Plotly Chart and Rate Limits")

        print("\n14. Exit")

        choice = input("\nChoose an exercise (1-14): ").strip()

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
            exercise_9()

        elif choice == "10":
            exercise_10()

        elif choice == "11":
            exercise_11()

        elif choice == "12":
            exercise_12()

        elif choice == "13":
            exercise_13()

        elif choice == "14":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 14.")


if __name__ == "__main__":
    main()
