import random

# Generate five consecutive numbers between 1 and 69
consecutive_numbers = list(range(1, 70))
random.shuffle(consecutive_numbers)
selected_consecutive_numbers = consecutive_numbers[:5]

# Generate one number between 1 and 26
random_number = random.randint(1, 26)

# Print the results
print("Five consecutive numbers between 1 and 69:", selected_consecutive_numbers)
print("One number between 1 and 26:", random_number)
