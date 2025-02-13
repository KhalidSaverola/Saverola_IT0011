def count_characters(input_string):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0
    spaces_count = 0
    others_count = 0
    
    for char in input_string:
        if char.isalpha():  
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
        elif char == ' ':
            spaces_count += 1
        else:
            others_count += 1

    print("Vowels:", vowels_count)
    print("Consonants:", consonants_count)
    print("Spaces:", spaces_count)
    print("Other characters:", others_count)


input_string = input("Enter a string: ")
count_characters(input_string)
