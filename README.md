# Student Record Manager

A Python console-based application designed to manage student records. This project demonstrates core programming concepts such as **Object-Oriented Programming (OOP)**, **File Handling**, **Regular Expressions (Regex)**, and **Exception Handling** in Python.

## Project Structure

```text
Student_Record_Manager/
│
├── main.py           # The entry point of the CLI application
├── student.py        # Defines the Student class representing student records
├── file_handler.py   # Handles reading and writing records to the students.txt file
├── validator.py      # Contains validation functions for all fields using regex & rules
└── README.md         # Documentation for the project
```

## Features

1. **Add Student Record**
   - User inputs Student ID, Name, Age, Email, and Course.
   - All fields are validated before storage.
   - Invalid values raise exceptions, print helper errors, and re-prompt the user.
2. **Robust Email Validation**
   - Implements regular expressions (`re` module) to validate user emails.
   - Example valid formats: `student@gmail.com`, `abc123@yahoo.com`, `john.doe@college.edu`.
   - Example invalid formats (rejected): `abc@gmail`, `@gmail.com`, `student.com`, `student@.com`.
3. **Persistent Storage**
   - Appends student records into `students.txt` in a readable format.
   - Prevents overwriting of existing student records.
4. **Display Stored Records**
   - Option to read and print all recorded student profiles.
   - Displays "No student records found." if `students.txt` is empty or doesn't exist.
5. **Crash-proof Exception Handling**
   - Catch all inputs errors (alphabetic ages, empty names/IDs, incorrect choices, etc.).
   - Top-level exception boundaries prevent the program from crashing.

## Validation Rules

- **Student ID**: Cannot be empty, must contain numbers only.
- **Name**: Cannot be empty, must contain alphabets and spaces only.
- **Age**: Integer value between 16 and 100 inclusive.
- **Email**: Must pass email regex pattern check.
- **Course**: Cannot be empty.

## How to Run

1. Make sure you have **Python 3.x** installed.
2. Open your terminal or command prompt in the project directory.
3. Run the following command:
   ```bash
   python main.py
   ```
4. Follow the interactive menu choices.
