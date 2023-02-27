def salary_schedule(start_salary, percent_increase, years):
    print("Year\tSalary") # header
    for year in range(1, years + 1):
        salary = start_salary * (1 + (percent_increase / 100) * (year - 1))
        print("{}\t${:,.2f}".format(year, salary))
        
# First year salary and 2 percent increase for 10 years
start_salary = 30000
percent_increase = 2
years = 10

salary_schedule(start_salary, percent_increase, years)
