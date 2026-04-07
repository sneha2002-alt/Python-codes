# Average of all numbers in the given list
num_list = []

total = 0

for num in num_list:
  total += num

if num_list:  
  avg = total / len(num_list)
  print(f"Average: {avg}")
else:
  print("Average: 0")

