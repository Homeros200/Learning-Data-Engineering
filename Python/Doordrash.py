gas_price = 4.32
miles = 11
pay = 15
tax = 30
avarage_mpg = 28
from decimal import Decimal

def income(miles, pay, time, gas_price = 4.32, avarage_mpg = 28, tax = 30 ):
    todays_income = []
    gallons_used = miles / avarage_mpg
    gas_cost = gallons_used * gas_price
    cost = pay - gas_cost
    result = cost - (cost * tax / 100)
    time_spent = str(time)
    return f"I earned ${result:.2f} in {time_spent} Hr/Min."
    

print(income(11,15,45))