import re

def validate_student_id(student_id: str) -> str:
    """
    Validates Student ID.
    Must not be empty and must contain only numbers.
    Raises ValueError if invalid.
    """
    cleaned_id = student_id.strip()
    if not cleaned_id:
        raise ValueError("Student ID cannot be empty.")
    if not cleaned_id.isdigit():
        raise ValueError("Student ID must contain only numbers.")
    return cleaned_id

def validate_name(name: str) -> str:
    """
    Validates Student Name.
    Must not be empty and must contain only alphabets and spaces.
    Raises ValueError if invalid.
    """
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("Name cannot be empty.")
    if not re.match(r"^[a-zA-Z\s]+$", cleaned_name):
        raise ValueError("Name must contain only alphabets and spaces.")
    return cleaned_name

def validate_age(age_str: str) -> int:
    """
    Validates Student Age.
    Must be an integer between 16 and 100.
    Raises ValueError if invalid.
    """
    cleaned_age = age_str.strip()
    if not cleaned_age:
        raise ValueError("Age cannot be empty.")
    try:
        age = int(cleaned_age)
    except ValueError:
        raise ValueError("Age must be a valid integer.")
    
    if age < 16 or age > 100:
        raise ValueError("Age must be between 16 and 100.")
    return age

def validate_email(email: str) -> str:
    """
    Validates Student Email.
    Uses regex to ensure correct email format.
    Raises ValueError if invalid.
    """
    cleaned_email = email.strip()
    if not cleaned_email:
        raise ValueError("Email address cannot be empty.")
    
    # Regex pattern matching validation rules
    # Must accept: student@gmail.com, abc123@yahoo.com, john.doe@college.edu
    # Must reject: abc@gmail, @gmail.com, student.com, student@.com
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9][a-zA-Z0-9.-]*\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, cleaned_email):
        raise ValueError("Invalid email format. (e.g. student@gmail.com)")
    return cleaned_email

def validate_course(course: str) -> str:
    """
    Validates Student Course.
    Must not be empty.
    Raises ValueError if invalid.
    """
    cleaned_course = course.strip()
    if not cleaned_course:
        raise ValueError("Course cannot be empty.")
    return cleaned_course
