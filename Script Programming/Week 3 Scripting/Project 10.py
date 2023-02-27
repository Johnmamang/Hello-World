# Input from the user
hourly_wage = float(input("Enter hourly wage: "))
regular_hours = float(input("Enter total regular hours: "))
overtime_hours = float(input("Enter total overtime hours: "))

#Calculate regular pay
regular_pay = hourly_wage * regular_hours

#Calculate overtime pay
overtime_pay = 1.5 * hourly_wage * overtime_hours

#Calculate total weekly pay
total_weekly_pay = regular_pay + overtime_pay

print("Total weekly pay: ${:.2f}".format(total_weekly_pay))
