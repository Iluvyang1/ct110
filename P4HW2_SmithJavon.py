# CTI-110
# P4HW2- Salary Calculator
# Javon Smith
# 5/7/23
#

# employee count, total overtime pay, total regular pay, and total gross pay
employee_count = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# loop for entering employee details
while True:
    # Input employee's name
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")
    
    # "Done" will break the loop
    if employee_name == "Done":
        break
    
    # hours worked and pay rate
    hours_worked = float(input("How many hours did {} work? ".format(employee_name)))
    pay_rate = float(input("What is {}'s pay rate? ".format(employee_name)))
    
    # Calculated overtime hours, overtime pay, regular hour pay, and gross pay
    overtime_hours = max(0, hours_worked - 40)
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_hour_pay = (hours_worked - overtime_hours) * pay_rate
    gross_pay = regular_hour_pay + overtime_pay
    
    # employee count, and update total overtime pay, total regular pay, and total gross pay
    employee_count += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_hour_pay
    total_gross_pay += gross_pay
    
    # Print employee details and calculated pay
    print("Employee name: {}".format(employee_name))
    print("Hours Worked \tPay Rate \tOverTime \tOverTime Pay \tRegHour Pay \tGross Pay")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("{:.1f} \t\t{:.2f} \t\t{:.1f} \t\t{:.2f} \t\t${:.2f}\t\t${:.2f}".format(hours_worked, pay_rate, overtime_hours, overtime_pay, regular_hour_pay, gross_pay))
    print()

# Print the summary of employee count, total overtime pay, total regular pay, and total gross pay
print("Total number of employees entered:", employee_count)
print("Total amount paid for overtime: ${:.2f}".format(total_overtime_pay))
print("Total amount paid for regular hours: ${:.2f}".format(total_regular_pay))
print("Total amount paid in gross: ${:.2f}".format(total_gross_pay))

