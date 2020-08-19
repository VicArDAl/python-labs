'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

inv_amount=float(input("investment amount: \n"))
print(inv_amount)
int_rate=float(input("interest rate in percentage: \n"))
print(int_rate, "percentage")
int_rate_percentage=int_rate/100

years_inv=float(input("number of years to invest: \n"))
print(years_inv)

fut_value=inv_amount*int_rate_percentage*years_inv
print("The future value is: ", inv_amount+fut_value)
