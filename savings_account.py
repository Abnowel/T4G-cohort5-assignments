from bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Creates the class savings account"""
    def _init_(self, account_holder, balance, interest_rate):
        super()._init_(account_holder, balance)
        self.interest_rate = interest_rate