# WAP to print all unique characters in a string and their count.
s = input("Enter a string: ")

char_count = {}

for char in s:
    char_count[char] = char_count.get(char, 0) + 1
   
print("Unique characters & their counts")

for char, count in char_count.items():
  print(f"'{char}': {count}")     