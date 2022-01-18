# Defining variables

class Loan:
    def __init__(self, amount, term, interest_rate):
        self.amount = amount
        self.term = term
        self.interest_rate = interest_rate


print("This mortgage calculator will help you calculate your monthly payments")
loan_principal = float(input(("What is your required loan principal? ")))
loans_term = int(input("What is your desired term(expressed in months)? "))


# yearly interest rate
def yearly_interest_rate(principal, term):
    if principal < 100000 and term < 60:
        return 5
    else:
        return 3


y_interest_rate = yearly_interest_rate(loan_principal, loans_term)
print(f"We can offer you an interest rate of {y_interest_rate} %")


# monthly interest rate
m_interest_rate = y_interest_rate / 1200
# number of monthly payments
loans_term = 360

# monthly payment
c_1 = m_interest_rate * loan_principal * (1 + m_interest_rate)**loans_term
c_2 = (1 + m_interest_rate)**loans_term - 1
c_total = c_1 / c_2

print(f"Your monthly paiment would be in amount of {c_total} $")
