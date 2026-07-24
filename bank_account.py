class BankAccount:
    """creating a class BankAccount"""
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance  = balance

    """Methods for managing a BankAccount instance"""
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero")
        self.balance += amount

    def withdraw(self,amount):
        if amount<= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds,Kindly load your account.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
    """Display when account is printed"""
    def __str__(self):
        return f"Account[{self.account_holder}]| Balance: GHS {self.balance:.2f}"

# Create two instances of the BankAccount class
account1 = BankAccount("Abnowel Sam", 700)
account2 = BankAccount("James Opoku", 2000)

# Make three transactions across the two accounts
account1.deposit(300)
account1.withdraw(70)
account2.deposit(400)

# Print the accouns after the transactions
print(account1)
print(account2)

# Try to withdraw more money than the account balance
try:
    account1.withdraw(1000)
except ValueError as error:
    print(f"Transaction failed: {error}")

    

    

        

        
        
        