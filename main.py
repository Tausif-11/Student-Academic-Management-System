import json 


# -----------------------------------------------------------------
# STUDENT MANAGEMENT SYSTEM IN PYTHON (BEGINNER FRIENDLY PROJECT)
# -----------------------------------------------------------------

"""
Concepts covered in this project:
 Concepts used:  - Variables  - Strings  - Integers / Floats  - Lists - Dictionaries  - Nested dictionaries  - if / elif / else  - for loops  - while loops - Functions  - try / except  - JSON  - Searching  - Updating data  - Calculations

"""
           #                   ============================================================ 
           #                                          JSON FUNCTIONS
           #                   ============================================================


STUDENTS_DATA = "students.json"

def load_students():
      """Load students from the JSON file."""

      try:
            with open(STUDENTS_DATA, "r") as file:
                  students = json.load(file)

            return students
      except FileNotFoundError:
            print("\nError: Students data file not found.")
            print("Please make sure the Students Data file exists in the correct location.")
            return []
      except json.JSONDecodeError:
            print("\nError: Students Data contain invalid JSON.")
            return []

def save_students(students):
      """Saves All Students Data to the JSON file."""


      try:
            with open(STUDENTS_DATA, "w") as file:
                  json.dump(students,file, indent=4)

            print("\nStudents data saved successfully.")

      except Exception as error:
            print("\nError: Unable to save students data.")




#                             ============================================================

#                                                    SEARCH FUNCTIONS

#                             ============================================================


def find_student(students, roll_number):
      """ Search for a student using roll number. """

      for student in students:
            if student["roll_number"] == roll_number:
                  return student

      return None

def get_roll_number():
      """Ask the user to add a valid roll number."""

      while True:

            try:
                  roll_number = int(input("Enter Roll Number:"))

                  if roll_number <= 0:
                        print('Roll number must be greater than 0. Please try again.')

                  else: 
                        return roll_number

            except ValueError:
                  print("Please enter a valid number for roll number. Try again.")



#                             ============================================================

#                                                  DISPLAY FUNCTIONS 

#                            ============================================================

def display_student_basic_information(student):
      'Display basic information of as student.'

      print("\n") 
      print("=" * 60) 
      print("               STUDENT INFORMATION") 
      print("=" * 60)

      print("Student Name:        ", student["student_name"])
      print("Roll Number:         ", student["roll_number"])
      print("Parent Name:         ", student["parent_name"])
      print("Contact Number:       ", student["contact_number"])
      print("Alternate Contact Number:", student["alternate_contact_number"])

      print("=" * 60)

def display_marks(student):
      'Display marks of a student.'

      print("\n")
      print("=" * 60)
      print("                   STUDENT MARKS")
      print("=" * 60)

      marks = student["marks"]

      for subject, score in marks.items():
            print(f"{subject:<25}: {score}")

      print("=" * 60)


#                             ============================================================

#                                                MARKS CALCULATION FUNCTIONS

#                             ============================================================

def calculate_total(marks):
      """Calculate the total marks of a student."""

      total = 0

      for subject in marks:
            total = total + marks[subject]

      return total

def calculate_percentage(marks):
      """ Calculate the percentage of a student based on marks. """

      total = calculate_total(marks)
      number_of_subjects = len(marks)
      maximum_marks = number_of_subjects * 100
      percentage = (total / maximum_marks) * 100
      return percentage

def calculate_grade(percentage):
      """ Calculate the grade of a student based on percentage. """

      if percentage >= 90:
            return "A+"
      elif percentage >= 80:
            return "A"
      elif percentage >= 70:
            return "B"
      elif percentage >= 60:
            return "C"
      elif percentage >= 50:
            return "D"
      elif percentage >= 40:
            return "E"
      else:
            return "F"
      

#                             ============================================================

#                                            DISPLAY INDIVIDUAL SCORE

#                             ============================================================


            

def check_individual_score(students):
      """Check the individual score of a student>"""

      print("\n)")
      print("=" * 60)
      print("               INDIVIDUAL STUDENT SCORE")
      print("=" * 60)

      roll_number = get_roll_number()

      student = find_student(students, roll_number)

      if student is None:
            print("\nStudent record not found")
            return 

      display_student_basic_information(student)

      print("\nMarks: ")

      marks = student["marks"]

      total = calculate_total(marks)
      percentage = calculate_total(marks)
      grade = calculate_grade(percentage)

      for subject, score in marks.items ():
            print(f"{subject:<25} : {score}")

      print("-" * 60)
      print(f"{'Total':<25} : {total}")
      print(f"{'Percentage':<25} : {percentage:.2f}%")
      print(f"{'Grade':<25} : {grade}")
      print("=" * 60)

#                        ============================================================         

#                                            REGISTER NEW STUDENT

#                        =============================================================

def register_new_student(students):
      "Register new students"

      print("\n")    
      print("="*60)
      print("                    REGISTER NEW STUDENT")
      print("="*60)


      # ---------------------
          # Roll Number
      # ---------------------

      while True:

            try: 
                  roll_number = int(input("Enter Roll Number: "))

                  if roll_number <=0:
                        print("Roll number must be greater than 0")
                        continue

                  existing_student = find_student(students,roll_number)

                  if existing_student is not None:
                        print("A student with this roll number already exists.")
                        return
                  break

            except ValueError :
                  print('Please enter a valid roll number.')

      #           -------------------------------------------------------- 
      #              STUDENT INFORMATION
      #           --------------------------------------------------------                 

      student_name = input("Enter Student Name: ")
      parent_name = input("Enter Parent Name: ")
      contact_number = (input("Enter Contact Number: "))
      alternate_contact_number = (input("Enter Alternate Contact Number: "))

      # --------------------------------------------------------
      #                       MARKS
      # --------------------------------------------------------

      print("\nEnter marks out of 100.")

      subjects = [ "English", "Mathematics", "Science & Technology", "Social Science", "Hindi" ]

      marks = {}

      for subject in subjects:
            while True:
                  try:
                        score= int(input(f"Enter Marks for {subject}:"))

                        if score < 0 or score > 100:
                              print("\nMarks must be between 0 & 100.")

                        else:
                              marks[subject]= score
                              break
                  except ValueError:        
                        print("Please enter a valid number.")

      # --------------------------------------------------------
      # Create Student Dictionary
      # --------------------------------------------------------    

      new_student = { "roll_number": roll_number, 
                     "student_name": student_name, 
                     "parent_name": parent_name, 
                     "contact_number": contact_number, 
                     "alternate_contact_number": alternate_contact_number, 
                     "marks": marks,
                       "semesters": {}, 
                       "attendance": {} 
                     }

      students.append(new_student)

      save_students(students)

      print("\nStudent registered successfully!")
      display_student_basic_information(new_student)

#                 ============================================================

#                                   REGISTER ATTENDANCE

#                  ============================================================


def register_attendance(students):

      print("\n")
      print("="*60)
      print("                     REGISTER ATTENDANCE")
      print("="*60)

      roll_number = get_roll_number()

      student = find_student(students,roll_number)

      if student is None:
            print("\nStudent Not Found")
            return

      print("\nStudent:", student["student_name"])

      semester = input("Enter Semester name/number:   ")

      semester = str(semester)

      while True:

            try:
                  total_classes = int(input("Enter Total Number of Classes:  "))

                  if total_classes < 0 :
                        print("Total Classes cannot be negative.")
                        continue

                  break
            except ValueError:
                  print("Please enter a valid number.")


      while True:
            try: 
                  attended_classes = int(input("Enter number of classes attended: "))

                  if attended_classes < 0 :
                        print("Attended classes cannot be negative.")
                        continue

                  if attended_classes > total_classes :
                        print("Attended classes cannot be greater than total classes.")
                        continue
                  break
            except ValueError: 
                  print("Please enter a valid number." )

             # Create attendance section if it doesn't exist

      if "attendance" not in student:
            student["attendance"]= {}

      student["attendance"]["semester"] = {
            "total_classes" : total_classes,
            "attended_classes": attended_classes
      }         
      save_students(students)

      print("\nAttendance Registered Successfully.")

                        # ============================================================

                        #                  ATTENDANCE PERCENTAGE

                        # ============================================================


def caluclate_attendance_percentage(total_classes, attended_classes):

      if total_classes == 0:
            return 0

      percentage = (attended_classes/total_classes)*100
      return percentage

def check_attendance_percentage(students):

      print("\n")
      print("="*60)
      print("                 ATTENDANCE PERCENTAGE")
      print("="*60)

      roll_number = get_roll_number()

      student = find_student(students, roll_number)

      if student is None:
            print("\nStudent not found.")
            return
      display_student_basic_information(student)

      if "attendance" not in student:
            print("\nNo Attendance Record Available.")
            return

      attendance = student["attendance"]

      if len(attendance) == 0:
            print("\nNo Attendance records avaialble.")
            return

      total_classes_all = 0
      attended_classes_all = 0

      print("\nAttendance Records")
      print("-"*60)

      for semester, data in attendance.items():

            total_classes = data["total_classes"]
            attended_classes = data["attended_classes"]

            percentage = caluclate_attendance_percentage(
                  total_classes,
                  attended_classes
            )

            print(f"Semester{semester}")
            print(f"Total: {total_classes}")
            print(f"Classes Attended: {attended_classes}")
            print(f"Attendance   :  {percentage: .2f}%")
            print("="*60)

            total_classes_all += total_classes
            attended_classes_all += attended_classes

      overall_percentage = caluclate_attendance_percentage(
            total_classes_all,
            attended_classes_all
      )
      print("\nOVERALL ATTENDANCE")

      print("-" * 60) 
      print("Total Classes :", total_classes_all) 
      print("Classes Attended :", attended_classes_all)
      print(f"Attendance : {overall_percentage:.2f}%")

      print("="*60)
      
#                       =========================================================================

#                                               ENTER MARKS FOR NEW SEMESTER

#                       =========================================================================

def enter_new_semester_marks(students):

      print("\n")
      print("="*60)
      print("                            ENTER NEW SEMESTER MARKS")
      print("=" * 60)

      roll_number = get_roll_number()

      student = find_student(students,roll_number)

      if student is None:
            print("\n Student Not Found.")
            return
      display_student_basic_information(student)

      semester = input("\nEnter New Semester Marks: ")

      if "semesters" not in student:
            student["semesters"] ={}

      if semester in student["semesters"]:
            print("\nThis Semester Already Exists.")

            choice = input("\n Do you want to overwrite it? (yes/no): ")

            if choice.lower() != "yes":
                  print("Operation cancelled.")
                  return

      subjects = [
            "English",
            "Mathematics",
            "Science & Technology",
            "Social Science",
            "Hindi"
      ]
      new_marks ={}
      print("\nEnter Marks Out Of 100.")

      for subject in subjects:
            while True:
                  try:
                        score = float(input(f"Enter marks for {subject}: "))
                        if score < 0 or score > 100:
                              print("\nMarks Must Be Between 0 & 100")

                        else:
                              new_marks[subject] = score
                              break
                  except ValueError:
                        print("\n Please Enter A Valid Number.")

      student["semesters"][semester] = { "marks": new_marks }    

      save_students(students)
      print("\nNew semester marks registered successfully!")

#                 ============================================================    
    
#                                   DISPLAY ALL SEMESTERS
              
#                 ============================================================    
        

















      

