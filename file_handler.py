import os
from student import Student

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "students.txt")

def save_student_record(student: Student) -> bool:
    """
    Appends the student record to the students.txt file.
    Returns True if saved successfully, False otherwise.
    """
    try:
        with open(FILE_PATH, "a", encoding="utf-8") as file:
            file.write(student.to_file_format())
        return True
    except PermissionError:
        print("\n[Error] Permission denied. Cannot write to 'students.txt'.")
        return False
    except IOError as e:
        print(f"\n[Error] Input/Output error while saving student: {e}")
        return False
    except Exception as e:
        print(f"\n[Error] An unexpected error occurred: {e}")
        return False

def read_student_records() -> str:
    """
    Reads all student records from students.txt.
    Returns the file content. If empty or doesn't exist, returns 'No student records found.'.
    """
    if not os.path.exists(FILE_PATH):
        return "No student records found."
    
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                return "No student records found."
            return content
    except FileNotFoundError:
        return "No student records found."
    except PermissionError:
        return "[Error] Permission denied. Cannot read 'students.txt'."
    except IOError as e:
        return f"[Error] Input/Output error while reading: {e}"
    except Exception as e:
        return f"[Error] An unexpected error occurred: {e}"
