limit = int(input("Enter a number: "))
odd_numbers = [num for num in range(limit) if num % 2 != 0]
print(odd_numbers)
