# Get user input
n = int(input("Enter a natural number n: "))

# Compute the sum using a loop
total_sum = 0
for i in range(1, n + 1):
    total_sum += i

# Print the result
print(f"The sum of natural numbers from 1 to {n} is {total_sum}.")
