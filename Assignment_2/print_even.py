# Program to print all even integers between a and b (inclusive).

def calc_even(a,b):
  for i in range(a,b+1):
    if(i % 2 == 0):
      print(i)

num1 = int(input("Enter 1st number: "))    
num2 = int(input("Enter 2nd number: "))    
calc_even(num1, num2)    