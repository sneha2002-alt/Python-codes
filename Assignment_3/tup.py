# Separate tuples of all even and odd numbers
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)

tup_even = []
tup_odd = []

for val in tup:
  if(val % 2 == 0):
    tup_even.append(val)
  else:
    tup_odd.append(val)
    
print("Even tuple:", tuple(tup_even))     
print("Odd tuple:", tuple(tup_odd))     