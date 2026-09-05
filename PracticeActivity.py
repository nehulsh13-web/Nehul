import random 
play = True 
random_number = str(random.randint(10,20))
print("You will have to guess a number from 10-50")
while play:
    choice = input("Enter a number ")
    if choice == random_number:
        print("You have won")
        break
    else:
        print("Try Again")



