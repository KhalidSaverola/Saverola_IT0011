# Program 2:
from datetime import datetime

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        formatted_date = date_obj.strftime("%B %d, %Y")
        print(f"Date Output: {formatted_date}")
    except ValueError:
        print("Invalid date format. Please enter the date in mm/dd/yyyy format.")

date_input = input("Enter the date (mm/dd/yyyy): ")
format_date(date_input)