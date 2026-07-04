import validator
import file_handler
from student import Student

def prompt_student_id() -> str:
    """
    Prompts the user for Student ID and validates it.
    Re-prompts until valid.
    """
    while True:
        try:
            val = input("Enter Student ID:\n")
            return validator.validate_student_id(val)
        except ValueError as e:
            print(f"[Error] {e}\n")

def prompt_name() -> str:
    """
    Prompts the user for Name and validates it.
    Re-prompts until valid.
    """
    while True:
        try:
            val = input("Enter Name:\n")
            return validator.validate_name(val)
        except ValueError as e:
            print(f"[Error] {e}\n")

def prompt_age() -> int:
    """
    Prompts the user for Age and validates it.
    Re-prompts until valid.
    """
    while True:
        try:
            val = input("Enter Age:\n")
            return validator.validate_age(val)
        except ValueError as e:
            print(f"[Error] {e}\n")

def prompt_email() -> str:
    """
    Prompts the user for Email and validates it.
    Re-prompts until valid.
    """
    while True:
        try:
            val = input("Enter Email:\n")
            return validator.validate_email(val)
        except ValueError as e:
            print(f"[Error] {e}\n")

def prompt_course() -> str:
    """
    Prompts the user for Course and validates it.
    Re-prompts until valid.
    """
    while True:
        try:
            val = input("Enter Course:\n")
            return validator.validate_course(val)
        except ValueError as e:
            print(f"[Error] {e}\n")

def main():
    try:
        while True:
            print("========= Student Record Manager =========")
            print()
            print("1. Add Student")
            print("2. View Students")
            print("3. Exit")
            print()
            
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                print()
                student_id = prompt_student_id()
                print()
                name = prompt_name()
                print()
                age = prompt_age()
                print()
                email = prompt_email()
                print()
                course = prompt_course()
                print()
                
                # Instantiate student object
                student = Student(student_id, name, age, email, course)
                
                # Save student
                if file_handler.save_student_record(student):
                    print("Student record saved successfully.\n")
                    
            elif choice == "2":
                records = file_handler.read_student_records()
                print(f"\n{records}\n")
                
            elif choice == "3":
                print("\nExiting the program. Goodbye!")
                break
            else:
                print("\n[Error] Invalid choice. Please enter 1, 2, or 3.\n")
                
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting gracefully. Goodbye!")
    except Exception as e:
        print(f"\n[Error] An unexpected critical error occurred: {e}")
        print("Exiting program.")

if __name__ == "__main__":
    main()
