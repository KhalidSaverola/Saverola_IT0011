import csv

def load_currency_rates(filename):
    rates = {}
    with open(filename, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            currency_code, currency_name, rate = row
            rates[currency_code] = float(rate)
    return rates

def convert_currency(usd_amount, target_currency, rates):
    if target_currency in rates:
        return usd_amount * rates[target_currency]
    else:
        return None


filename = "currency.csv"
rates = load_currency_rates(filename)


usd_amount = float(input("How much dollar do you have? "))
target_currency = input("What currency you want to have? ").upper()

converted_amount = convert_currency(usd_amount, target_currency, rates)

if converted_amount is not None:
    print(f"Dollar: {usd_amount} USD")
    print(f"{target_currency}: {converted_amount}")
else:
    print("Currency not found.")
