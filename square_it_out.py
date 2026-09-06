def find_and_filter_squares(start, end):
   
    even_squares = []
    odd_squares = []

    for num in range(start, end + 1):
        square = num ** 2
        
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
            

    print(f"Squares from {start} to {end}:")
    print(f"Even squares: {even_squares}")
    print(f"Odd squares:  {odd_squares}")

# Example usage:
find_and_filter_squares(1, 10)
