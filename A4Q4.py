# Set the initial number of pieces to 0
pieces = 0

# Check the number of pieces for each possible divisor
for divisor in range(5, 8):
  # Calculate the number of pieces
  pieces = divisor * (divisor - 2)
  
  # If the number of pieces is less than 200, break the loop
  if pieces < 200:
    break

# Print the result
print("There are", pieces, "pieces of candy in the bowl.")
