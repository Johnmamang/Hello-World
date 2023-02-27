def read_payroll_file(filename):
    with open(filename, 'r') as f:
        # initialize a list to store the employee information
        employees = []
        # loop over each line in the file
        for line in f:
            # split the line into three fields: last name, hourly wage, and hours worked
            fields = line.strip().split()
            last_name = fields[0]
            hourly_wage = float(fields[1])
            hours_worked = float(fields[2])
            # calculate the wages paid for this employee
            wages_paid = hourly_wage * hours_worked
            # add the employee information and wages paid to the list
            employees.append((last_name, hours_worked, wages_paid))
        return employees

def print_payroll_report(employees):
    # print the header of the report
    print("Name\tHours Worked\tWages Paid")
    print("====\t============\t===========")
    # loop over the employee information and print it in tabular format
    for employee in employees:
        last_name, hours_worked, wages_paid = employee
        print(f"{last_name}\t{hours_worked:.2f}\t\t{wages_paid:.2f}")

# example usage
filename = input("Enter the filename: ")
employees = read_payroll_file(filename)
print_payroll_report(employees)
