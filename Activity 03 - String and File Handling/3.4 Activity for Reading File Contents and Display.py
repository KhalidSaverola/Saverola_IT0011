try:
    with open("students.txt", "r") as file:
        print("\nReading Student Information:\n")
        print(file.read())
except FileNotFoundError:
    print("Error: The file 'students.txt' does not exist.")