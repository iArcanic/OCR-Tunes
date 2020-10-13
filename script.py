def integer_validation(x, y):
    global user_integer_input
    while True:
        print("Welcome to OCR Tunes! \n Please enter a time length for your Pop playlist. e.g. 5 for 5 mins etc. Max 10 mins.")
        user_integer_input = input(f"Enter a number between {x} and {y}: ")
        if not user_integer_input.isdigit():
            print("Invalid input. Must be an integer. \n")
            continue
        user_integer_input = int(user_integer_input)
        if x <= user_integer_input <= y:
            break
        print(f"Invalid input. Must be an integer between {x} and {y}. \n")
    return user_integer_input


def string_validation(string):
    global user_string_input
    while True:
        user_string_input = string
        if user_string_input.isdigit():
            print("Invalid input. Must be a string. \n")
            continue
        if user_string_input[0].islower():
            print("Invalid input. First letter must be capitalised. \n")
            continue
        spaces = " " in user_string_input
        if not spaces:
            break
        print("Invalid input. Must not contain any spaces. \n")
    return user_integer_input