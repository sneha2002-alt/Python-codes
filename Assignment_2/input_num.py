# Program to continuously input a no. n from user & print if it is positive or negative until the user enters "Quit".

while True:
  n = input("Enter a number: ")

  if n == "quit":
    break

  n = int(n)

  if n > 0:
    print("The number is positive")
  elif n < 0:
    print("The number is negative")
  else:
    print("Zero is neither positive nor negative")