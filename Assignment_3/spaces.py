# WAP that takes a string and prints the number of spaces in the string
s = input("Enter a string: ")
count = 0

for i in s:
  if(i == " "):
    count += 1
  
print("Total no. of spaces in string =", count)  
