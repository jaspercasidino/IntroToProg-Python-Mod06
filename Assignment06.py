# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   AWysocki,02/13/24, Modified code to work with json files for HW5, added error handling
#   AWysocki,02/21/24, Modified code for HW6 to work with functions
# ------------------------------------------------------------------------------------------ #

import json
import io as _io

# Define the Global variables
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
file = _io.TextIOWrapper

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = ""  # Hold the choice made by the user.

class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            # Extract the data from the file
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("File to open does not exist!\n", e)
        except Exception as e:
            IO.output_error_messages("There is a non-specific error!\n", e)
        finally:
            return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
class IO:
    @staticmethod
    def output_menu(menu: str):
        # Displays menu that is passed in
        print(menu)

    @staticmethod
    def input_menu_choice():
        # Asks user for menu choice and returns that value as a str
        choice = input("What would you like to do: ")
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        # Asks user for first name, last name, and course number then appends that information to student_data table
        # that is passed in as a parameter and returns the appended data as a list
        try:
            student_first_name = input("Enter the student's first name: ")
            if student_first_name.isalpha() == False:
                raise ValueError("First Name should not contain numbers!")
            student_last_name = input("Enter the student's last name: ")
            if student_last_name.isalpha() == False:
                raise ValueError("Last Name should not contain numbers!")
            course_name = input("Please enter the name of the course: ")
            student_info = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            student_data.append(student_info)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            return student_data
        except ValueError as e:
            IO.output_error_messages(e)  # Prints the custom message
        except Exception as e:
            IO.output_error_messages("There was a non-specific error",e)

    @staticmethod
    def output_student_courses(student_data: list):
        # Displays the current student information in memory
        print("-" * 50)
        for student in student_data:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-" * 50)

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        # Displays error message to deal with Exception handling
        print(f"{message}")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_from_file(FILE_NAME, students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        IO.input_student_data(students)

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME,students)

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")



