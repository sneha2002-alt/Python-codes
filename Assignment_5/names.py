# with open("Names.txt", "w") as f:
#   for i in range(5):
#     name = input(f"Enter name {i + 1}: ")
#     f.write(name + "\n")

with open("Names.txt", "r") as f:
  for i in range(5):
    print(f.readline().strip())