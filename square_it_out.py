def find_and_filter_squares(start, end):
    # Lists to store the filtered square values
    even_squares = []
    odd_squares = []
    
    # Iterate through the range of numbers (inclusive of the end value)
    for num in range(start, end + 1):
        square = num ** 2
        
        # Filter into even or odd lists
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
            
    # Print the final results
    print(f"Squares from {start} to {end}:")
    print(f"Even squares: {even_squares}")
    print(f"Odd squares:  {odd_squares}")

# Example usage:
find_and_filter_squares(1, 10)
