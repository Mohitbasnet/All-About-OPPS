# Problem-5: Write a program with class Bill.
#  The users have the option to pay the bill either by cheque or by cash. 
# Use the inheritance to model this situation.

class Bill:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        raise NotImplementedError("Subclasses must implement pay() method")


class ChequeBill(Bill):
    def __init__(self, amount, cheque_number):
        super().__init__(amount)
        self.cheque_number = cheque_number

    def pay(self):
        print(f"Paid by Cheque of amount {self.amount} with Cheque Number {self.cheque_number}")


class CashBill(Bill):
    def pay(self):
        print(f"Paid by Cash of amount {self.amount}")


# Example usage:
if __name__ == "__main__":
    # Creating instances of bills
    cheque_bill = ChequeBill(1000, "123456")
    cash_bill = CashBill(1500)

    # Paying bills
    cheque_bill.pay()  # Output: Paid by Cheque of amount 1000 with Cheque Number 123456
    cash_bill.pay()    # Output: Paid by Cash of amount 1500
