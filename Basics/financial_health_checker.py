# Mini project : Financial Health Checker

# Taking Input
monthly_income = int(input("Enter your monthly income = "))
rent = int(input("Enter your monthly rent = "))
food_expense = int(input("Enter your monthly expense on food = "))
other_expense = int(input("Enter your other expenses = "))

# Arithmetic Operations
total_expense = rent + food_expense + other_expense
net_savings = monthly_income - total_expense

# Calculating percentages
saving_percentage = (net_savings/monthly_income)*100
rent_precision = (rent/monthly_income)*100

# Checking Financial Health using logical operators
is_saving_healthy = saving_percentage >= 20               # If saving_percentage is >=20 then true else false
is_rent_high = rent_precision >= 30                       # # If is_rent_high is >=30 then true else false
can_invest = net_savings >= 5000 and is_saving_healthy    #  # # If can_invest is >=5000 & is_saving_healthy is true then true else false

# Printing Output in a neat format
print("\nYour total monthly income is ", monthly_income)
print("Your total monthly expense is ",total_expense)
print("\nYour Net savings is = ", net_savings)
print("You saved ",saving_percentage,"percent of your monthly income.")
print("Is your saving rate is healthy ? = ",is_saving_healthy)
print("Is your rent is high ? = ",is_rent_high)
print("Can you invest ? = ", can_invest)

# Output
# Enter your monthly income = 25000
# Enter your monthly rent = 5000
# Enter your monthly expense on food = 3000
# Enter your other expense including entertainment,EMIs,etc = 2000
# Your total monthly income is  25000
# Your total monthly expense is  10000
# Your Net savings is =  15000
# You saved  60.0 percent of your monthly income.
# Is your saving rate is healthy ? =  True
# Is your rent is high ? =  False
# Can you invest ? =  True