
# Print the 2 and 3 multiplication tables using a nested for-loop

# Outer loop for the numbers 2 and 3
for num in range(2, 4):
    print(f"Multiplication Table for {num}:")
    
    # Inner loop for multiplying by numbers 1 through 10
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    
    print()  # Print a blank line for better readability