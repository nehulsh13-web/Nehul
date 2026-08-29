num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
def larger_num(num_1,num_2):
    if num_1 > num_2:
        print ("The greater number is", num_1)
    elif num_2 > num_1:
        print ("The greater number is", num_2)
    else:
        print ("Both are equal")  
larger_num(num1, num2)
