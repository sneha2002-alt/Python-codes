# Function to count the number of digits in a number, n.
def count_digit(n):
    if (n == 0):
        return 1
      
    n = abs(n)  # Handle negative numbers
    count = 0
    while(n != 0):
      n = n // 10
      count += 1
    return count     
  
num = int(input("Enter number: ")) 
print(count_digit(num)) 