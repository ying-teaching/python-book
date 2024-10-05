"""
A simple course enrollment application that uses a dictionary
where the keys are course names and values are sets of
enrolled student names.
"""

course_enrollments = {
    "Math": {"Alice", "Bob"},
    "Science": {"Bob", "Charlie"},
    "History": {"Alice", "David"},
}


# 1. Add a student to a course
def enroll_student():
    """Enroll a student in a course"""

    course = input("Enter the course name: ")
    student = input("Enter the student's name: ")
    if course not in course_enrollments:
        course_enrollments[course] = set()  # Create a new course if not exists
    course_enrollments[course].add(student)
    print(f"Enrolled {student} in {course}")


def is_student_enrolled():
    """Check if a student is enrolled in a course"""

    course = input("Enter the course name: ")
    student = input("Enter the student's name: ")

    is_enrolled = student in course_enrollments.get(course, set())
    if is_enrolled:
        print(f"{student} is enrolled in {course}")
    else:
        print(f"{student} is not enrolled in {course}")


def remove_student():
    """Remove a student from a course"""
    course = input("Enter the course name: ")
    student = input("Enter the student's name: ")
    if course in course_enrollments and student in course_enrollments[course]:
        course_enrollments[course].remove(student)
        print(f"Removed {student} from {course}")
    else:
        print(f"{student} is not enrolled in {course}")


def display_students():
    """Display all students in a course"""

    course = input("Enter the course name: ")
    students = course_enrollments.get(course, set())
    if students:
        print(f"Students enrolled in {course}: {', '.join(students)}")
    else:
        print(f"No students enrolled in {course}")


def main():
    """Main function for user interaction"""
    while True:
        print("\n--- Course Enrollment System ---")
        print("1. Enroll a student in a course")
        print("2. Check if a student is enrolled in a course")
        print("3. Remove a student from a course")
        print("4. Display all students in a course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        match choice:
            case "1":
                enroll_student()
            case "2":
                is_student_enrolled()
            case "3":
                remove_student()
            case "4":
                display_students()
            case "5":
                print("Exiting the system. Goodbye!")
                break
            case _:
                print("Invalid choice! Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()
