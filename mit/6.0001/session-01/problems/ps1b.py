# Saving, with a raise
# Going to build on the solution to part A by factoring
# in a raise every six months.

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary ' + 
        'to save as a decimal (e.g. .10): '))
total_cost = float(input('Enter the total cost of the house: '))
semi_annual_raise = float(input('Enter the semi-annual raise, ' +
    'as a decmial: '))

def update_annual_salary(annual_salary, percentage):
    return annual_salary + (annual_salary * percentage)

def calculate_monthly_savings(annual_salary, portion_saved):
    return (annual_salary * portion_saved) / 12

portion_down_payment = 0.25
current_savings = 0
down_payment_goal = total_cost * portion_down_payment
monthly_savings = calculate_monthly_savings(annual_salary, portion_saved)
months_to_save = 0

while current_savings < down_payment_goal:
    if months_to_save > 0 and months_to_save % 6 == 0:
        annual_salary = update_annual_salary(annual_salary, semi_annual_raise)
        monthly_savings = calculate_monthly_savings(
                annual_salary,
                portion_saved)
    current_savings += monthly_savings + (current_savings * 0.04 / 12)
    months_to_save += 1

print('Number of months: %d' % months_to_save)

