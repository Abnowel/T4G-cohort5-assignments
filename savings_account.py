from bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Creates the class savings account"""
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    # Calculates interest based on the current balance and adds the interest to the account.
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

    # Displays the savings account details and interest rate.
    def __str__(self):
        return f"SavingsAccount[{self.account_holder}] | Balance: GHS {self.balance:.2f} | Rate: {self.interest_rate}%"

# Create a savings account with a starting balance and interest rate.
savings = SavingsAccount("Abnowel", 700, 5)

# Make two deposits.
savings.deposit(400)
savings.deposit(300)

# Apply interest to the current balance.
savings.apply_interest()

# Print the account after applying interest.
print(savings)

# Make a withdrawal 
try:
    savings.withdraw(70)
    print("Withdrawal successful.")
except ValueError as error:
    print(f"Transaction failed: {error}")

# Print the account after the withdrawal.
print(savings)