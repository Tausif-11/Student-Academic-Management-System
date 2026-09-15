# Student Academic Management System

A beginner-friendly **Student Academic Management System** built using Python.

This project demonstrates how fundamental Python concepts can be combined to create a larger, practical application without using classes, OOP, databases, or external frameworks.

---

## 📌 Project Overview

The Student Academic Management System allows users to manage student information, marks, semesters, attendance, and academic performance.

Student data is stored in a **JSON file**, while Python handles the program logic, calculations, searching, updating, and user interaction.

---

## ✨ Features

- Register new students
- Store student and parent information
- Store primary and alternate contact numbers
- Enter marks for five subjects
- Check individual student scores
- Register attendance
- Calculate attendance percentage
- Add marks for new semesters
- Calculate semester percentage
- Calculate overall academic percentage
- Calculate grades
- Search students by roll number
- Search students by name
- Display all registered students
- Generate a complete student report card
- Automatically save updated data to JSON
- Input validation and error handling

---

## 📚 Subjects

The system currently manages marks for:

- English
- Mathematics
- Science & Technology
- Social Science
- Hindi

---

## 🛠️ Technologies Used

- **Python 3**
- **JSON**
- Git & GitHub

---

## 🧠 Python Concepts Demonstrated

This project was intentionally developed using fundamental Python concepts:

- Variables
- Strings
- Integers
- Floats
- Lists
- Dictionaries
- Nested dictionaries
- `if / elif / else`
- `for` loops
- `while` loops
- Functions
- `try / except`
- User input
- Searching
- Data manipulation
- Mathematical calculations
- File handling
- JSON handling

### No Advanced Concepts

This project does **not** currently use:

- Classes
- Object-Oriented Programming
- Databases
- Pandas
- External frameworks

The goal is to demonstrate how simple Python concepts can be combined to build a relatively large application.

---

## 📂 Project Structure

```text
Student-Academic-Management-System/
│
├── main.py
├── students.json
├── LICENSE
└── README.md
main.py

Contains the complete Python program and all application logic.

students.json

Contains the student database in JSON format.

LICENSE

Contains the MIT License for the project.

README.md

Contains documentation and information about the project.

▶️ How to Run
1. Clone the repository
git clone https://github.com/Tausif-11/Python-Notes-All-Concepts.git
2. Navigate to the project directory
cd Python-Notes-All-Concepts
3. Make sure these files are together
main.py
students.json
4. Run the program
python main.py
🖥️ Main Menu

When the program starts, the user can choose from:

1.  Register New Student
2.  Register Attendance
3.  Check Individual Scores
4.  Enter Marks for New Semester
5.  Calculate Semester Percentage
6.  Calculate Overall Percentage
7.  Calculate Attendance Percentage
8.  Generate Full Student Report
9.  Student Information / Search
10. Exit
💾 Data Storage

The project uses students.json to store student information.

Python loads the data when the program starts:

with open("students.json", "r") as file:
    students = json.load(file)

Whenever information is added or updated, the program saves the updated data back into the JSON file.

📊 Academic Calculations

The system can calculate:

Total Marks
Total = Sum of all subject marks
Percentage
Percentage = (Total Marks / Maximum Marks) × 100
Attendance
Attendance Percentage =
(Classes Attended / Total Classes) × 100
Overall Percentage

The current version calculates the overall percentage by taking the average of the recorded semester percentages.

🎓 Grade System

The current grading system is:

Percentage	Grade
90–100%	A+
80–89%	A
70–79%	B
60–69%	C
50–59%	D
40–49%	E
Below 40%	F
🔐 License

This project is licensed under the MIT License.

See the LICENSE file for more information.

🚀 Future Improvements

Possible future improvements include:

Better user interface
Student result editing
Student deletion
Subject management
More detailed report cards
Data validation improvements
Exporting reports
Graphical User Interface (GUI)
Database integration
Object-Oriented Programming
Authentication and user accounts

👨‍💻 Author 


Mohammad Tausif

Built as a Python learning project to practice fundamental programming concepts and develop a practical, larger-scale application.
