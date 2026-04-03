# Number guessing game
num = int(input("Enter the number: "))

while True:
  n = int(input("Guess the number!: "))

  if (n == num):
    print("Correct!")
    break
  elif (n > num):
    print("Too high")
  else:
    print("Too low")