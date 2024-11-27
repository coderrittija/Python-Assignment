def determine_character_type(char):
    if 'A' <= char <= 'Z':
        return "Capital Letter"
    elif 'a' <= char <= 'z':
        return "Small Letter"
    elif '0' <= char <= '9':
        return "Digit"
    else:
        return "Special Symbol"
char = input("Enter a character: ")
if len(char) == 1:
    result = determine_character_type(char)
    print(f"The character is: {result}")
else:
    print("Please enter a single character.")