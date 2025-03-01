import csv

# Load currency exchange rates from currency.csv
def load_currency_rates(file_path):
    exchange_rates = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            currency, rate = row
            exchange_rates[currency] = float(rate)
    return exchange_rates

# Convert USD to selected currency
def convert_currency(amount, target_currency, rates):
    if target_currency in rates:
        return amount * rates[target_currency]
    else:
        return None

# Main Program
file_path = "C:\Users\lenovo\Downloads\currency.csv"
rates = load_currency_rates(file_path)

usd_amount = float(input("How much dollar do you have? "))
target_currency = input("What currency do you want to have? ")

converted_amount = convert_currency(usd_amount, target_currency, rates)

if converted_amount is not None:
    print(f"\nDollar: {usd_amount} USD")
    print(f"{target_currency}: {converted_amount}")
else:
    print("Currency not found in the list.")
