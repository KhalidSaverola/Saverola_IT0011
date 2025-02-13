# Program 1: 
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def check_palindrome_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            status = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {status}")
    except FileNotFoundError:
        print("File not found. Please make sure numbers.txt exists.")

check_palindrome_in_file('numbers.txt')