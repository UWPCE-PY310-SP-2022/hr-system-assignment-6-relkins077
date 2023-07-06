import csv
import datetime


def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Load Employees from CSV")
        print("2. Save Employees to CSV")
        print("3. Add New Employee")
        print("4. Generate Report of Current Employees")
        print("5. Generate Report of Recently Left Employees")
        print("6. Generate Report of Annual Review Reminders")
        print("7. Quit")

        choice = input("Choose an option from the list below: ")

        if choice == "1":
            load_employees()
        elif choice == "2":
            save_employees()
        elif choice == "3":
            add_employee()
        elif choice == "4":
            report_current_employees()
        elif choice == "5":
            report_recently_left()
        elif choice == "6":
            report_annual_review_reminders()
        elif choice == "7":
            break  # Exit the loop to quit
        else:
            print("Invalid option, please try again.")


# create data storage variable
employees = []


def load_employees():
    file_path = input("Please provide the full path of the CSV file (or type 'exit' to return to main menu): ")
    if file_path.lower() == 'exit':
        return
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Change the strings to appropriate data types
            row['employee_id'] = int(row['employee_id'])
            row['date_of_birth'] = datetime.datetime.strptime(row['date_of_birth'], '%m/%d/%Y')
            row['start_date'] = datetime.datetime.strptime(row['start_date'], '%m/%d/%Y')
            row['end_date'] = None if row['end_date'] == '' else datetime.datetime.strptime(row['end_date'], '%m/%d/%Y')
            employees.append(row)


def save_employees():
    file_path = input("Please provide the full path of the CSV file (or type 'exit' to return to main menu): ")
    if file_path.lower() == 'exit':
        return
    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=employees[0].keys())
        writer.writeheader()
        for employee in employees:
            # Change the dates to string before writing
            employee['date_of_birth'] = employee['date_of_birth'].strftime('%m/%d/%Y')
            employee['start_date'] = employee['start_date'].strftime('%m/%d/%Y')
            employee['end_date'] = '' if employee['end_date'] is None else employee['end_date'].strftime('%m/%d/%Y')
            writer.writerow(employee)


def add_employee():
    new_employee = {'name': input("Enter the name of the employee: ")}
    if new_employee['name'].lower() == 'exit':
        return
    new_employee['address'] = input("Enter the address of the employee: ")
    new_employee['ssn'] = input("Enter the SSN of the employee: ")
    new_employee['date_of_birth'] = datetime.datetime.strptime(
        input("Enter the date of birth of the employee (MM/DD/YYYY): "), '%m/%d/%Y')
    new_employee['job_title'] = input("Enter the job title of the employee: ")
    new_employee['start_date'] = datetime.datetime.now()  # Assuming that the start date is today
    new_employee['end_date'] = None
    new_employee['employee_id'] = max(
        employee['employee_id'] for employee in employees) + 1  # Generating a new unique id
    employees.append(new_employee)


import csv
import datetime


def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Load Employees from CSV")
        print("2. Save Employees to CSV")
        print("3. Add New Employee")
        print("4. Generate Report of Current Employees")
        print("5. Generate Report of Recently Left Employees")
        print("6. Generate Report of Annual Review Reminders")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            load_employees()
        elif choice == "2":
            save_employees()
        elif choice == "3":
            add_employee()
        elif choice == "4":
            report_current_employees()
        elif choice == "5":
            report_recently_left()
        elif choice == "6":
            report_annual_review_reminders()
        elif choice == "7":
            break  # Exit the loop to quit
        else:
            print("Invalid option, please try again.")


# create data storage variable
employees = []


def load_employees():
    file_path = input("Please provide the full path of the CSV file (or type 'exit' to return to main menu): ")
    if file_path.lower() == 'exit':
        return
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Change the strings to appropriate data types
            row['employee_id'] = int(row['employee_id'])
            row['date_of_birth'] = datetime.datetime.strptime(row['date_of_birth'], '%m/%d/%Y')
            row['start_date'] = datetime.datetime.strptime(row['start_date'], '%m/%d/%Y')
            row['end_date'] = None if row['end_date'] == '' else datetime.datetime.strptime(row['end_date'], '%m/%d/%Y')
            employees.append(row)


def save_employees():
    file_path = input("Please provide the full path of the CSV file (or type 'exit' to return to main menu): ")
    if file_path.lower() == 'exit':
        return
    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=employees[0].keys())
        writer.writeheader()
        for employee in employees:
            # Change the dates to string before writing
            employee['date_of_birth'] = employee['date_of_birth'].strftime('%m/%d/%Y')
            employee['start_date'] = employee['start_date'].strftime('%m/%d/%Y')
            employee['end_date'] = '' if employee['end_date'] is None else employee['end_date'].strftime('%m/%d/%Y')
            writer.writerow(employee)


def add_employee():
    new_employee = {'name': input("Enter the name of the employee: ")}
    if new_employee['name'].lower() == 'exit':
        return
    new_employee['address'] = input("Enter the address of the employee: ")
    new_employee['ssn'] = input("Enter the SSN of the employee: ")
    new_employee['date_of_birth'] = datetime.datetime.strptime(
        input("Enter the date of birth of the employee (MM/DD/YYYY): "), '%m/%d/%Y')
    new_employee['job_title'] = input("Enter the job title of the employee: ")
    new_employee['start_date'] = datetime.datetime.now()  # Assuming that the start date is today
    new_employee['end_date'] = None
    new_employee['employee_id'] = max(
        employee['employee_id'] for employee in employees) + 1  # Generating a new unique id
    employees.append(new_employee)


def report_current_employees():
    print("Current Employees:")
    for employee in employees:
        if employee['end_date'] is None:
            print_employee_info(employee)


def report_recently_left():
    print("Employees left within the past 31 days:")
    for employee in employees:
        if employee['end_date'] is not None and (datetime.datetime.now() - employee['end_date']).days <= 31:
            print_employee_info(employee)


def report_annual_review_reminders():
    print("Employees whose work anniversary is within 90 days:")
    for employee in employees:
        start_date = employee['start_date']
        if employee['end_date'] is None:
            current_date = datetime.datetime.now().date()
            anniversary_date = datetime.date(current_date.year, start_date.month, start_date.day)
            if (anniversary_date - current_date).days <= 90:
                print_employee_info(employee)


def print_employee_info(employee):
    print(f"Name: {employee['name']}")
    print(f"Address: {employee['address']}")
    print(f"SSN: {employee['ssn']}")
    print(f"Date of Birth: {employee['date_of_birth'].strftime('%m/%d/%Y')}")
    print(f"Job Title: {employee['job_title']}")
    print(f"Start Date: {employee['start_date'].strftime('%m/%d/%Y')}")
    print(f"End Date: {'N/A' if employee['end_date'] is None else employee['end_date'].strftime('%m/%d/%Y')}")
    print(f"Employee ID: {employee['employee_id']}")
    print("------------------------------")


if __name__ == "__main__":
    main_menu()



if __name__ == "__main__":
    main_menu()
