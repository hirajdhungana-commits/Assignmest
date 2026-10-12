students = [
    {"name": "Alice", "marks": {"Math": 85, "Science": 90, "English": 78}},
    {"name": "Bob", "marks": {"Math": 72, "Science": 68, "English": 80}},
    {"name": "Charlie", "marks": {"Math": 95, "Science": 88, "English": 92}},
    {"name": "Diana", "marks": {"Math": 60, "Science": 75, "English": 70}},
    {"name": "Ethan", "marks": {"Math": 50, "English": 65}},
]


def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    raise ValueError(f"Student '{name}' does not exist in the system.")


def calculate_total(student):
    total = 0
    missing = []
    for subject, mark in student["marks"].items():
        if mark is None:
            missing.append(subject)
        else:
            total += mark
    if missing:
        print(f"Warning: missing marks for {', '.join(missing)} (counted as 0).")
    return total


def calculate_percentage(student):
    total = calculate_total(student)
    max_mastudents = [
    {"name": "Alice", "marks": {"Math": 85, "Science": 90, "English": 78}},
    {"name": "Bob", "marks": {"Math": 72, "Science": 68, "English": 80}},
    {"name": "Charlie", "marks": {"Math": 95, "Science": 88, "English": 92}},
    {"name": "Diana", "marks": {"Math": 60, "Science": 75, "English": 70}},
    {"name": "Ethan", "marks": {"Math": 50, "English": 65}},
]


def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    raise ValueError(f"Student '{name}' does not exist in the system.")


def calculate_total(student):
    total = 0
    missing = []
    for subject, mark in student["marks"].items():
        if mark is None:
            missing.append(subject)
        else:
            total += mark
    if missing:
        print(f"Warning: missing marks for {', '.join(missing)} (counted as 0).")
    return total


def calculate_percentage(student):
    total = calculate_total(student)
    max_mastudents = [
    {"name": "Alice", "marks": {"Math": 85, "Science": 90, "English": 78}},
    {"name": "Bob", "marks": {"Math": 72, "Science": 68, "English": 80}},
    {"name": "Charlie", "marks": {"Math": 95, "Science": 88, "English": 92}},
    {"name": "Diana", "marks": {"Math": 60, "Science": 75, "English": 70}},
    {"name": "Ethan", "marks": {"Math": 50, "English": 65}},
]


def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    raise ValueError(f"Student '{name}' does not exist in the system.")


def calculate_total(student):
    total = 0
    missing = []
    for subject, mark in student["marks"].items():
        if mark is None:
            missing.append(subject)
        else:
            total += mark
    if missing:
        print(f"Warning: missing marks for {', '.join(missing)} (counted as 0).")
    return total


def calculate_percentage(student):
    total = calculate_total(student)
    max_marks = len(student["marks"]) * 100
    return (total / max_marks) * 100


def main():
    name = input("Enter student name: ").strip()
    try:
        student = find_student(name)
    except ValueError as error:
        print(error)
        return

    total = calculate_total(student)
    percentage = calculate_percentage(student)
    print(f"\nStudent : {student['name']}")
    print(f"Total   : {total}")
    print(f"Percent : {percentage:.2f}%")


if __name__ == "_main_":
    main()