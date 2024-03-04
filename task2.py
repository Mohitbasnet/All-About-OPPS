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
