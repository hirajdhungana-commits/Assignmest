employees = {
    "101": {"name": "Alice", "department": "HR", "salary": 3000},
    "102": {"name": "Bob", "department": "IT", "salary": 4500},
    "103": {"name": "Charlie", "department": "Finance", "salary": 5200},
    "104": {"name": "Diana", "department": "IT", "salary": 6000},
    "105": {"name": "Ethan", "department": "Sales", "salary": 3800},
}


def find_employee(emp_id):
    if emp_id not in employees:
        raise KeyError(f"Employee ID '{emp_id}' does not exist.")
    return employees[emp_id]


def calculate_yearly(employee):
    return employee["salary"] * 12


def increase_salary(employee, percent):
    old = employee["salary"]
    employee["salary"] = old + (old * percent / 100)
    return old


def main():
    emp_id = input("Enter employee ID: ").strip()
    try:
        employee = find_employee(emp_id)
    except KeyError as error:
        print(f"Error: {error}")
        return

    print(f"\nEmployee  : {employee['name']}")
    print(f"Department: {employee['department']}")
    print(f"Salary    : {employee['salary']:.2f}")

    try:
        percent = float(input("Enter salary increase %: "))
        old = increase_salary(employee, percent)
        print(f"\nOld salary   : {old:.2f}")
        print(f"New salary   : {employee['salary']:.2f}")
        print(f"Yearly salary: {calculate_yearly(employee):.2f}")
    except ValueError:
        print("Invalid percentage. Please enter a number.")


if __name__ == "__main__":
    main()