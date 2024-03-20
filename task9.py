from datetime import datetime

class Product:
    def __init__(self, manufacturing_date, expiry_date):
        self.manufacturing_date = manufacturing_date
        self.expiry_date = expiry_date

    def calculate_remaining_time(self):
        today = datetime.today()
        remaining_time = self.expiry_date - today

        years = remaining_time.days // 365
        months = (remaining_time.days % 365) // 30
        days = (remaining_time.days % 365) % 30

        return years, months, days

# Example usage:
if __name__ == "__main__":
    # Input manufacturing date and expiry date (yyyy, mm, dd)
    manufacturing_date = datetime(2022, 3, 1)
    expiry_date = datetime(2024, 3, 1)

    product = Product(manufacturing_date, expiry_date)
    years, months, days = product.calculate_remaining_time()

    print(f"Years left for expiry: {years}")
    print(f"Months left for expiry: {months}")
    print(f"Days left for expiry: {days}")
