# Program to calculate tax rate on different salaries.
sal = int(input("Enter salary(in thousands):"))

if(sal < 30000):
  tax_rate = sal * 0.05 #5%
elif(30000 <= sal < 70000):
  tax_rate = sal * 0.15 #15%
else:
  tax_rate = sal * 0.25 #25%
  
print("Final tax rate =", tax_rate)    
  