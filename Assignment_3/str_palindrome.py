# WAP to check if a string is palindrome or not.
s = input("Enter a string: ")

rev_str = ""

for ch in s:
  rev_str = ch + rev_str
  
print("Reversed string is:",rev_str)  

if (s == rev_str):
  print("It is a palindrome")
else:
  print("Not a palindrome")  
  