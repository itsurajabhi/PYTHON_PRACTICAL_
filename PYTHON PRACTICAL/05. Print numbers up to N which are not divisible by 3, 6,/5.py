

number = int(input("Enter a number: "))

# Check if the number is divisible by both 3 and 5
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")

