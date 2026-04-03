# Calculator
def calculator(a, b, op):
  if op == "+":
    return a + b
  elif op == "-":
    return a - b
  elif op == "*":
    return a * b
  elif op == "/":
    if b == 0:
      return "Error: Division by zero is not allowed"
      return a / b
    else:
      return "Error: Invalid operation"
    

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = calculator(num1, num2, operation)
print("Result:", result)    