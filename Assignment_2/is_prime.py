# WAP to check number is prime or not.
def is_prime(n):
    if n < 2:
      return False    
           
    for i in range(2, n):  # loop from 2 to n-1
        if (n % i == 0):        
          return False     # n is not prime
    return True            # no divisor found => n is prime
  
num = int(input("Enter number: "))  
print(is_prime(num))   