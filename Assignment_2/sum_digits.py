# Function to return the sum of digits of a number, n.
def sum_of_digits(n):
    if (n == 0):
        return 0
      
    n = abs(n)  # Handle negative numbers
    sum = 0
    while(n != 0):
      i = n % 10
      sum += i
      n = n // 10
    
    return sum    
  
num = int(input("Enter number: ")) 
print("Sum =",sum_of_digits(num)) 