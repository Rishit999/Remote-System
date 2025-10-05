num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

print(f"\nResults:")
print(f"Addition of {num1} and {num2} = {addition}")
print(f"Subtraction of {num1} and {num2} = {subtraction}")
print(f"Multiplication of {num1} and {num2} = {multiplication}")
print(f"Division of {num1} and {num2} = {division}")
