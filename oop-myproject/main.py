from student import Student


def main():
    all_students = []

    while True:
        name = input("Enter the student's name: ")
        student = Student(name)

        while True:
            subject = input("Enter the subject: ")
            while True:
                try:
                    score = float(input("Enter the score for the subject (0-20): "))
                    if 0 <= score <= 20:
                        break  # End loop if score is valid
                    else:
                        print("Score must be between 0 and 20. Please enter a valid score.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            student.add_subject(subject, score)

            # Ask if the student wants to add another subject
            another_subject = input("Do you want to add another subject? (yes/no): ").strip().lower()
            if another_subject != 'yes':
                break

        all_students.append(student)

        # Ask if there is a new student
        new_student = input("Is there a new student? (yes/no): ").strip().lower()
        if new_student != 'yes':
            break

    # Print all students' results
    print("\nAll Students' Results:")
    for student in all_students:
        print(student)


if __name__ == "__main__":
    main()