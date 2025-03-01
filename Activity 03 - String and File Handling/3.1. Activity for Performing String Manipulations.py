first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

full_name = first_name + " " + last_name

sliced_name = first_name[:3]

greeting_message = f"Hello, {sliced_name}! Welcome. You are {age} years old."

print("\nFull Name:", full_name)
print("Sliced Name:", sliced_name)
print("Greeting Message:", greeting_message)