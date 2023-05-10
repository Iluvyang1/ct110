    # This program calculates and displays the travel expenses and remaining balance
    # 4-28-2023
    # CTI-110 P1HW1 - Travel Expense
    # Javon Smith
print("This program calculates and displays travel expenses")
# enter user budget
budget = float(input("Enter your budget : "))
# enter user destination
destination = input("Enter your destination : ")
# enter user gas expenses
gas_expenses = float(input("How much you will spend on gas : "))
# enter users living expenses
accomodation = float(input("Approximately how much you need for accomodation ? : "))
# enter user food expenses
food_expenses = float(input("Last, how much do you need for food? : "))
# calculate remaining balance after other expenses
remaining_balance = budget - gas_expenses - accomodation - food_expenses    
print("------------------------------travel expenses----------------------------------")
print("Location : " + destination)
print("Initial budget : " + str(budget))
print()
print("Fuel : " + str(gas_expenses))
print("Accomodation : " + str(accomodation))
print("Food : " + str(food_expenses))
print()
print("Remaining balance : " + str(remaining_balance))
