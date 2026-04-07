# WAP to check whether two lists share no common elements.

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 4]

l1 = set(list_1)
l2 = set(list_2)

if(l1.intersection(l2) == set()):
  print("Both lists do not share any common elements.")
else:
  print("Both lists share common elements.")  