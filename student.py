class Student:
    """
    A class to represent a student record.
    """
    def __init__(self, student_id: str, name: str, age: int, email: str, course: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.course = course

    def display_student(self) -> str:
        """
        Returns a formatted string representing the student details for console display.
        """
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Email: {self.email}\n"
            f"Course: {self.course}"
        )

    def to_file_format(self) -> str:
        """
        Returns a formatted string suitable for saving to the text file.
        """
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Email: {self.email}\n"
            f"Course: {self.course}\n"
            f"------------------------\n"
        )
