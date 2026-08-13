def shutdown(user_input): 
    cleaned_input = user_input.lower().strip() 
    
    if cleaned_input == "yes": 
        print("shutting down") 
    elif cleaned_input == "no":
        print("abort shut down") 
    else: 
        print("sorry")

response = input("Do you want to shut down? (yes/no): ")
shutdown(response)
