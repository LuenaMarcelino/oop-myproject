from grades import Grades  # Assuming Grades is in grades.py

class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []  # List to store Grades objects

    def add_subject(self, subject: str, score: float) -> None:
        """Add a subject and its score to the student."""
        # Create a Grades object for each subject
        self.grades.append((subject, Grades([score])))

    def calculate_average(self) -> float:
        """Calculate the average score across all subjects."""
        if not self.grades:
            return 0.0
        total_average = sum(grade[1].calculate_average() for grade in self.grades)
        return total_average / len(self.grades)

    def is_pass(self) -> bool:
        """Determine if the student has passed based on the average score."""
        return self.calculate_average() >= 10

    def __str__(self) -> str:
        """String representation of the Student object."""
        return (f"Name: {self.name}, "
                f"Average: {self.calculate_average():.2f}, "
                f"Pass: {'Yes' if self.is_pass() else 'No'}, "
                f"Grades: {', '.join(str(grade[1]) for grade in self.grades)}")