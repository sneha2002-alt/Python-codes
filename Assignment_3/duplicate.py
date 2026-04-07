# WAP to print all elements that appear more than once in the list.

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
  nums = int(input(f"Enter element {i+1}: "))
  numbers.append(nums)
  
print("\nOriginal List:",numbers)
 
# Find duplicates using sets
unique_set = set()
duplicate_set = set()

for num in numbers:
  if num in unique_set:
    duplicate_set.add(num)
  else:
    unique_set.add(num)  
    
print(f"Elements appearing more than once are {duplicate_set}")    