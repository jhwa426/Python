"""
Jaeyoung Hwang (Jeff)

Compleate the program so that it calculates
the monthly repayments that need to be made to pay off a house loan.
"""





loan_amount = 650000 
annual_interest_rate = 5
loan_length_years = 20
month_per_year = 12

monthly_interest_rate = annual_interest_rate / month_per_year
total_period = loan_length_years * month_per_year

number_of_payments = loan_amount * (((monthly_interest_rate / 100) * (1 + monthly_interest_rate / 100)
                                    ** total_period) / ((1+monthly_interest_rate/100)** total_period -1))


print("You will need to pay $", round(number_of_payments), " monthly", sep="")
