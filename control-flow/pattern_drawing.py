# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the pattern using while and for loops
while row < size:
    # Print asterisks in the current row
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after completing the row
    print()
    
    # Increment row counter
    row += 1