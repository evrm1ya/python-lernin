# House Hunting
# Write a program to calculate how many months
# it will take to save up enough money for
# a down payment on a house.

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary ' + 
        'to save as a decimal (e.g. .10): '))
total_cost = float(input('Enter the total cost of the house: '))

portion_down_payment = 0.25
current_savings = 0
down_payment_goal = total_cost * portion_down_payment
monthly_savings = (annual_salary * portion_saved) / 12
months_to_save = 0

while current_savings < down_payment_goal:
    current_savings += monthly_savings + (current_savings * 0.04 / 12)
    months_to_save += 1

print('Number of months: %d' % months_to_save)

