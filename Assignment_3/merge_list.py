# Merge two lists into one ans sort the result
# List 1 input
s1 = int(input("Size of list 1: "))
list1 = []

for i in range(s1):
    num = int(input(f"List 1 element {i+1}: "))
    list1.append(num)

# List 2 input  
s2 = int(input("Size of list 2: "))
list2 = []

for i in range(s2):
    num = int(input(f"List 2 element {i+1}: "))
    list2.append(num)

# Merge and sort
merge_list = list1 + list2
merge_list.sort()

print("Merged sorted list:", merge_list)