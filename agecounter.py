def check_user_age():
    user_input = input("Please enter your age: ")
    
    try:
        age = int(user_input)
        
        if age % 2 == 0:
            print(f"Success! The age {age} is a valid integer and it is an EVEN number.")
        else:
            print(f"Success! The age {age} is a valid integer and it is an ODD number.")
            
    except ValueError:
        print("ValueError: Invalid input! Please enter a valid whole number (no decimals, letters, or special characters).")

check_user_age()
