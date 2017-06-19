# Finding the right amount to save away
# Want to set a particular goal, e.g. be able to
# afford the down payment in three years.
# How much should be saved each month to achieve this?

# Find the best rate of savings to achieve a down payment
# on a $1M house in 36 months. Hitting this exactly is a
# challenge, so savings should be within $100 of the
# required down payment.

annual_salary = float(input('Enter your annual salary: '))
cost_of_house = 1000000
semi_annual_raise = .07
annual_return = 0.04
down_payment = 0.25 * cost_of_house

# Searching for a value that is a float.
# Limit to 2 decimals of accuracy.
# ex.) 7.04% - 7.041% and 7.039% work
# Can search for an integer between 0 to 10000
# using integer division, and then convert it to
# a decimal percentage using float division to use
# when calculating current_savings after 36 months.
# 704 / 10000.0 == 0.0704

def calculate_raise(annual_salary, percentage):
    return annual_salary + (annual_salary * percentage)

def calculate_monthly_savings(annual_salary, portion_saved):
    return (annual_salary * portion_saved) / 12

def return_on_investments(current_savings):
    return (current_savings * annual_return) / 12

def savings_after_three_years(annual_salary, portion_saved):
    months = 0
    current_savings = 0
    monthly_savings = calculate_monthly_savings(annual_salary, portion_saved)
    while months < 36:
        if months > 0 and months % 6 == 0:
            annual_salary = calculate_raise(annual_salary, semi_annual_raise)
            monthly_savings = calculate_monthly_savings(
                    annual_salary,
                    portion_saved)
        current_savings += monthly_savings + \
                           return_on_investments(current_savings)
        months += 1
    return current_savings

def bisection_search(annual_salary, down_payment):
    epsilon = 100
    minimum = 0
    maximum = 10000
    average = (maximum + minimum) / 2
    numGuesses = 0
    while maximum > minimum:
        numGuesses += 1
        savings_rate = average / 10000.0
        savings = savings_after_three_years(annual_salary, savings_rate)
        if abs(savings - down_payment) < epsilon:
            return {'savings': savings,
                    'numGuesses': numGuesses,
                    'savings_rate': savings_rate}
        if savings < down_payment - epsilon:
            minimum = average + 1
        if savings > down_payment + epsilon:
            maximum = average - 1
        average = (maximum + minimum) / 2
    return 'This annual salary is too low.'

print(bisection_search(annual_salary, down_payment))

