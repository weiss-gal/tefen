# Read input from the user
user_input = input("What would you like to solve? ")
num1, sign, num2 = user_input.split()

# Convert the numbers to integers
num1 = int(num1)
num2 = int(num2)

# Check the sign and perform the operation
result = None

if sign == "+":
    result = num1 + num2
elif sign == "-":
    result = num1 - num2
elif sign == "*":
    result = num1 * num2
elif sign == "/":
    result = num1 / num2
else:
    print("Invalid sign")

# Print the result
if result is not None:
    print(result)