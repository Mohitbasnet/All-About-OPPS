
# Q-2: Bank Class
# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details. Give the complete code for the BankAccount class.
# Eg. After making above classes and methods, on executing below code:-

# newAccount = BankAccount(2178514584, "Mandy" , 2800)

# newAccount.Withdrawal(700)

# newAccount.Deposit(1000)

# newAccount.display()
# Output:

# Account Number :  2178514584
# Account Name :  Mandy
# Account Balance :  3100 ₹

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs. {amount} successful.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of Rs. {amount} successfully. ")

            else:
                print("Insufficient balance.")

        else:
            print("Withdrawal amount must be greater than zero")

    def bank_fees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print(f"Bank fees of Rs. {fee} applied.")

    def display(self):
        print("Account Number:", self.accountNumber)
        print("Account Name:", self.name)
        print("Account Balance: Rs", self.balance)


newAccount = BankAccount(23425325, "Mohit", 100000)
newAccount.withdraw(50000)
newAccount.deposit(10000)
newAccount.display()
