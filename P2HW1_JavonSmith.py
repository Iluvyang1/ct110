# This program calculates and displays travel expenses and remaining balance
    # 4-28-2023
    # CTI-110 P2HW1 - Travel Expense
    # Javon Smith
    #
print("This program calculates and displays travel expenses")
budget = float(input("Enter your budget : "))   # reading user budget
destination = input("Enter your destination : ")    # reading user destination
gas_expenses = float(input("How much you will spend on gas : "))    # reading user fuel expenses
accomodation = float(input("Approximately how much you need for accomodation ? : "))    # reading user hostel expenses
food_expenses = float(input("Last, how much do you need for food? : "))     # reading user food expenses
remaining_balance = budget - gas_expenses - accomodation - food_expenses    # calculating remaining balance
print("------------------------------travel expenses----------------------------------")
print("Location : " + destination)
print("Initial budget : " + str(budget))
print()
print("Fuel : " + str(gas_expenses))
print("Accomodation : " + str(accomodation))
print("Food : " + str(food_expenses))
print()
print("Remaining balance : " + str(remaining_balance))
