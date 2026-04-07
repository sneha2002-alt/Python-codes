# WAP to print all unique characters in a string and their count.
s = input("Enter a string: ")

char_count = {}

for char in s:
  if char in char_count:
    char_count[char] += 1
  else:
    char_count[char] = 1  
    
print("Unique characters & their counts")

for char, count in char_count.items():
  print(f"'{char}': {count}")    