# Function that prints digits of a number, n.

def print_digit(n):
  if(n == 0):
    print(0)
    return
  digits = []
  while(n != 0):
    digits.append(n % 10)
    n = n // 10
  
  #Print original sequence
  for digit in reversed(digits):
    print(digit)
  
num = int(input("Enter number:"))   
print_digit(num)   