from bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Creates the class savings account"""
    def _init_(self, account_holder, balance, interest_rate):
        super()._init_(account_holder, balance)
        self.interest_rate = interest_rate

    # Calculates interest based on the current balance and adds the interest to the account.
    def apply_interest(self):
        interest = self.starting_balance * (self.interest_rate / 100)
        self.deposit(interest)

    # Displays the savings account details and interest rate.
    def _str_(self):
        return f"SavingsAccount[{self.account_holder}] | Balance: GHS {self.starting_balance:.2f} | Rate: {self.interest_rate}%"